"""
SCENARIO 3: Code needing documentation.

This module contains complex but poorly documented code.
The agent should generate comprehensive documentation.

Ask the AI agent: "Generate comprehensive documentation for this module
including docstrings, type hints improvements, and a module-level overview"
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Pipeline(Generic[T, U]):
    def __init__(self, transforms=None):
        self._transforms = transforms or []

    def add(self, transform):
        self._transforms.append(transform)
        return self

    def __or__(self, other):
        if isinstance(other, Pipeline):
            return Pipeline(self._transforms + other._transforms)
        elif callable(other):
            return Pipeline(self._transforms + [other])
        raise TypeError(f"Cannot combine Pipeline with {type(other)}")

    def __call__(self, data):
        result = data
        for transform in self._transforms:
            result = transform(result)
        return result


class Transform(ABC, Generic[T, U]):
    @abstractmethod
    def __call__(self, data: T) -> U:
        pass

    def __or__(self, other):
        return ComposedTransform(self, other)


class ComposedTransform(Transform[T, U]):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __call__(self, data):
        return self.second(self.first(data))


class FilterTransform(Transform[list[T], list[T]]):
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, data):
        return [item for item in data if self.predicate(item)]


class MapTransform(Transform[list[T], list[U]]):
    def __init__(self, mapper):
        self.mapper = mapper

    def __call__(self, data):
        return [self.mapper(item) for item in data]


class ReduceTransform(Transform[list[T], U]):
    def __init__(self, reducer, initial=None):
        self.reducer = reducer
        self.initial = initial

    def __call__(self, data):
        if self.initial is not None:
            result = self.initial
            for item in data:
                result = self.reducer(result, item)
            return result
        else:
            iterator = iter(data)
            result = next(iterator)
            for item in iterator:
                result = self.reducer(result, item)
            return result


class GroupByTransform(Transform[list[dict], dict[Any, list[dict]]]):
    def __init__(self, key):
        self.key = key

    def __call__(self, data):
        groups = {}
        for item in data:
            k = item[self.key] if isinstance(self.key, str) else self.key(item)
            if k not in groups:
                groups[k] = []
            groups[k].append(item)
        return groups


class SortTransform(Transform[list[T], list[T]]):
    def __init__(self, key=None, reverse=False):
        self.key = key
        self.reverse = reverse

    def __call__(self, data):
        return sorted(data, key=self.key, reverse=self.reverse)


class WindowTransform(Transform[list[T], list[list[T]]]):
    def __init__(self, size, step=None):
        self.size = size
        self.step = step or size

    def __call__(self, data):
        windows = []
        i = 0
        while i + self.size <= len(data):
            windows.append(data[i:i + self.size])
            i += self.step
        return windows


class FlattenTransform(Transform[list[list[T]], list[T]]):
    def __init__(self, depth=1):
        self.depth = depth

    def __call__(self, data):
        def flatten_once(lst):
            result = []
            for item in lst:
                if isinstance(item, list):
                    result.extend(item)
                else:
                    result.append(item)
            return result

        result = data
        for _ in range(self.depth):
            result = flatten_once(result)
        return result


class CacheTransform(Transform[T, T]):
    def __init__(self, cache_key=None):
        self._cache = {}
        self._key_fn = cache_key or (lambda x: id(x))

    def __call__(self, data):
        key = self._key_fn(data)
        if key not in self._cache:
            self._cache[key] = data
        return self._cache[key]

    def clear(self):
        self._cache.clear()


class BatchTransform(Transform[list[T], list[list[T]]]):
    def __init__(self, batch_size):
        self.batch_size = batch_size

    def __call__(self, data):
        return [
            data[i:i + self.batch_size]
            for i in range(0, len(data), self.batch_size)
        ]


def pipe(*transforms):
    return Pipeline(list(transforms))


def identity():
    return lambda x: x


def compose(*funcs):
    def composed(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return composed


class LazyPipeline(Generic[T, U]):
    def __init__(self, source, transforms=None):
        self._source = source
        self._transforms = transforms or []

    def map(self, mapper):
        return LazyPipeline(self._source, self._transforms + [MapTransform(mapper)])

    def filter(self, predicate):
        return LazyPipeline(self._source, self._transforms + [FilterTransform(predicate)])

    def take(self, n):
        def taker(data):
            return data[:n]
        return LazyPipeline(self._source, self._transforms + [taker])

    def skip(self, n):
        def skipper(data):
            return data[n:]
        return LazyPipeline(self._source, self._transforms + [skipper])

    def collect(self):
        result = self._source() if callable(self._source) else self._source
        for transform in self._transforms:
            result = transform(result)
        return result

    def __iter__(self):
        return iter(self.collect())

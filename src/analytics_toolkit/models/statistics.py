"""Statistical calculations and utilities."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class StatisticsResult:
    """Container for statistical results."""

    mean: float
    median: float
    std_dev: float
    variance: float
    min_val: float
    max_val: float
    count: int


def calculate_mean(values: list[float]) -> float:
    """Calculate arithmetic mean of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def calculate_median(values: list[float]) -> float:
    """Calculate median of values."""
    if not values:
        return 0.0
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 0:
        return sorted_values[mid]
    return sorted_values[mid]


def calculate_variance(values: list[float], population: bool = True) -> float:
    """
    Calculate variance of values.

    Args:
        values: List of numeric values.
        population: If True, calculate population variance, else sample variance.

    Returns:
        Variance value.
    """
    if len(values) < 2:
        return 0.0

    mean = calculate_mean(values)
    squared_diff_sum = sum((x - mean) ** 2 for x in values)

    return squared_diff_sum / len(values)


def calculate_std_dev(values: list[float], population: bool = True) -> float:
    """Calculate standard deviation."""
    return math.sqrt(calculate_variance(values, population))


def calculate_percentile(values: list[float], percentile: int) -> float:
    """
    Calculate the nth percentile of values.

    Args:
        values: List of numeric values.
        percentile: Percentile to calculate (0-100).

    Returns:
        Percentile value.
    """
    if not values:
        return 0.0

    sorted_values = sorted(values)
    n = len(sorted_values)

    index = (percentile / 100) * n
    return sorted_values[int(index)]


def calculate_mode(values: list[float]) -> float | None:
    """Calculate mode (most frequent value)."""
    if not values:
        return None

    frequency: dict[float, int] = {}
    for v in values:
        frequency[v] = frequency.get(v, 0) + 1

    max_count = max(frequency.values())
    for v, count in frequency.items():
        if count == max_count:
            return v
    return None


def normalize_values(values: list[float]) -> list[float]:
    """Normalize values to 0-1 range."""
    if not values:
        return []

    min_val = min(values)
    max_val = max(values)

    range_val = max_val - min_val
    return [(v - min_val) / range_val for v in values]


def calculate_correlation(x: list[float], y: list[float]) -> float:
    """Calculate Pearson correlation coefficient between two lists."""
    if len(x) != len(y):
        raise ValueError("Lists must have same length")

    n = len(x)
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    denominator_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))

    return numerator / (denominator_x * denominator_y)


def compute_statistics(values: list[float]) -> StatisticsResult:
    """Compute comprehensive statistics for a list of values."""
    if not values:
        raise ValueError("Cannot compute statistics for empty list")

    return StatisticsResult(
        mean=calculate_mean(values),
        median=calculate_median(values),
        std_dev=calculate_std_dev(values),
        variance=calculate_variance(values),
        min_val=min(values),
        max_val=max(values),
        count=len(values),
    )

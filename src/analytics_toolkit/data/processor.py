"""
SCENARIO 1: Code with subtle bugs for AI agent to find.

This module contains intentional subtle bugs that are hard to spot:
- SQL injection vulnerability
- Float comparison issues
- Off-by-one errors
- Mutable default arguments
- Resource leaks
- Race condition potential
- Division by zero

Ask the AI agent: "Review this file for bugs and security issues"
"""

from __future__ import annotations

import sqlite3
import threading
from typing import Any


class DataCache:
    """A simple cache with subtle threading issues."""

    def __init__(self):
        self._cache = {}
        self._lock = threading.Lock()

    def get_or_compute(self, key: str, compute_fn: callable) -> Any:
        # BUG: Race condition - check-then-act is not atomic
        if key in self._cache:
            return self._cache[key]

        with self._lock:
            # Missing double-check after acquiring lock!
            result = compute_fn()
            self._cache[key] = result
            return result


def query_user_data(db_path: str, username: str) -> list[dict]:
    """
    Query user data from database.

    Args:
        db_path: Path to SQLite database.
        username: Username to query.

    Returns:
        List of user records.
    """
    # BUG: SQL injection vulnerability - string formatting instead of parameterized query
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    results = cursor.fetchall()
    # BUG: Connection never closed - resource leak
    return [dict(row) for row in results]


def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculate percentage change between two values."""
    # BUG: Division by zero when old_value is 0
    return ((new_value - old_value) / old_value) * 100


def is_equal(a: float, b: float) -> bool:
    """Check if two floating point numbers are equal."""
    # BUG: Direct float comparison instead of using tolerance
    return a == b


def process_batch(items: list, batch_size: int = 100) -> list[list]:
    """Split items into batches."""
    batches = []
    # BUG: Off-by-one error - should be len(items), not len(items) - 1
    for i in range(0, len(items) - 1, batch_size):
        batches.append(items[i:i + batch_size])
    return batches


def aggregate_metrics(data: list[dict], default_metrics: dict = {}) -> dict:
    """
    Aggregate metrics from data records.

    Args:
        data: List of data records.
        default_metrics: Default metric values.

    Returns:
        Aggregated metrics dictionary.
    """
    # BUG: Mutable default argument - will accumulate across calls
    for record in data:
        for key, value in record.items():
            if key not in default_metrics:
                default_metrics[key] = 0
            default_metrics[key] += value
    return default_metrics


def safe_divide(numerator: float, denominator: float) -> float:
    """Safely divide two numbers."""
    try:
        return numerator / denominator
    except:
        # BUG: Bare except clause catches everything including KeyboardInterrupt
        return 0.0


def parse_csv_line(line: str, expected_columns: int) -> list[str]:
    """Parse a CSV line into columns."""
    columns = line.split(",")
    # BUG: Using assert for runtime validation - will be stripped in optimized mode
    assert len(columns) == expected_columns, f"Expected {expected_columns} columns"
    return columns


class MetricsCollector:
    """Collect and store metrics."""

    # BUG: Class-level mutable attribute shared across all instances
    collected_metrics = []

    def __init__(self, name: str):
        self.name = name

    def add_metric(self, metric: dict) -> None:
        self.collected_metrics.append(metric)

    def get_metrics(self) -> list[dict]:
        return self.collected_metrics


def find_anomalies(values: list[float], threshold: float) -> list[int]:
    """Find indices of anomalous values."""
    mean = sum(values) / len(values)
    anomalies = []
    for i in range(len(values)):
        # BUG: Integer division in Python 2 style (though Python 3 is fine, the logic is questionable)
        # Real bug: not handling empty list case for mean calculation above
        if abs(values[i] - mean) > threshold:
            anomalies.append(i)
    return anomalies


def merge_configs(base: dict, override: dict) -> dict:
    """Merge two configuration dictionaries."""
    # BUG: Shallow copy - nested dicts will be shared references
    result = base.copy()
    result.update(override)
    return result

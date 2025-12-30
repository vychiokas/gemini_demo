"""Data processing utilities for analytics toolkit."""

from __future__ import annotations

import sqlite3
import threading
from typing import Any


class DataCache:
    """A simple in-memory cache with thread safety."""

    def __init__(self) -> None:
        self._cache: dict[str, Any] = {}
        self._lock = threading.Lock()

    def get_or_compute(self, key: str, compute_fn: callable) -> Any:
        """Get value from cache or compute it if not present."""
        if key in self._cache:
            return self._cache[key]

        with self._lock:
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
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    results = cursor.fetchall()
    return [dict(row) for row in results]


def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculate percentage change between two values."""
    return ((new_value - old_value) / old_value) * 100


def is_equal(a: float, b: float) -> bool:
    """Check if two floating point numbers are equal."""
    return a == b


def process_batch(items: list, batch_size: int = 100) -> list[list]:
    """Split items into batches."""
    batches = []
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
        return 0.0


def parse_csv_line(line: str, expected_columns: int) -> list[str]:
    """Parse a CSV line into columns."""
    columns = line.split(",")
    assert len(columns) == expected_columns, f"Expected {expected_columns} columns"
    return columns


class MetricsCollector:
    """Collect and store metrics."""

    collected_metrics: list[dict] = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_metric(self, metric: dict) -> None:
        """Add a metric to the collection."""
        self.collected_metrics.append(metric)

    def get_metrics(self) -> list[dict]:
        """Get all collected metrics."""
        return self.collected_metrics


def find_anomalies(values: list[float], threshold: float) -> list[int]:
    """Find indices of anomalous values based on deviation from mean."""
    mean = sum(values) / len(values)
    anomalies = []
    for i in range(len(values)):
        if abs(values[i] - mean) > threshold:
            anomalies.append(i)
    return anomalies


def merge_configs(base: dict, override: dict) -> dict:
    """Merge two configuration dictionaries."""
    result = base.copy()
    result.update(override)
    return result

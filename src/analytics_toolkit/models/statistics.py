"""
SCENARIO 2: Iterative problem-solving.

This module has multiple bugs that require iterative fixing.
The tests will fail initially, and the agent needs to fix them one by one.

Ask the AI agent: "Run the tests for this module and fix all failing tests"
"""

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
    # BUG 1: Integer division issue in edge case
    return sum(values) / len(values)


def calculate_median(values: list[float]) -> float:
    """Calculate median of values."""
    if not values:
        return 0.0
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    # BUG 2: Incorrect median calculation for even-length lists
    if n % 2 == 0:
        return sorted_values[mid]  # Should average mid-1 and mid
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

    # BUG 3: Sample variance should divide by n-1, population by n
    # Currently always divides by n regardless of population flag
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

    # BUG 4: No validation that percentile is in valid range
    sorted_values = sorted(values)
    n = len(sorted_values)

    # BUG 5: Incorrect percentile index calculation
    index = (percentile / 100) * n
    return sorted_values[int(index)]  # Should handle interpolation


def calculate_mode(values: list[float]) -> float | None:
    """Calculate mode (most frequent value)."""
    if not values:
        return None

    frequency = {}
    for v in values:
        frequency[v] = frequency.get(v, 0) + 1

    # BUG 6: Returns first max instead of handling ties properly
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

    # BUG 7: Division by zero when all values are the same
    range_val = max_val - min_val
    return [(v - min_val) / range_val for v in values]


def calculate_correlation(x: list[float], y: list[float]) -> float:
    """Calculate Pearson correlation coefficient between two lists."""
    if len(x) != len(y):
        raise ValueError("Lists must have same length")

    # BUG 8: Not handling edge case of len < 2
    n = len(x)
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    denominator_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))

    # BUG 9: Division by zero if std dev is 0
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

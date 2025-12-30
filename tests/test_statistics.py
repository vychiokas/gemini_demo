"""
Tests for statistics module.

These tests expose the bugs in the statistics module.
Run with: pytest tests/test_statistics.py -v
"""

from __future__ import annotations

import math

import pytest

from src.analytics_toolkit.models.statistics import (
    calculate_correlation,
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_percentile,
    calculate_std_dev,
    calculate_variance,
    compute_statistics,
    normalize_values,
)


class TestCalculateMean:
    """Tests for calculate_mean function."""

    def test_mean_basic(self) -> None:
        """Test basic mean calculation."""
        assert calculate_mean([1, 2, 3, 4, 5]) == 3.0

    def test_mean_empty(self) -> None:
        """Test mean of empty list."""
        assert calculate_mean([]) == 0.0

    def test_mean_single(self) -> None:
        """Test mean of single value."""
        assert calculate_mean([5]) == 5.0

    def test_mean_floats(self) -> None:
        """Test mean with float values."""
        assert calculate_mean([1.5, 2.5, 3.5]) == 2.5


class TestCalculateMedian:
    """Tests for calculate_median function."""

    def test_median_odd_length(self) -> None:
        """Test median for odd-length list."""
        assert calculate_median([1, 3, 5, 7, 9]) == 5.0

    def test_median_even_length(self) -> None:
        """Test median for even-length list - should average middle values."""
        # Median of [1, 2, 3, 4] should be (2+3)/2 = 2.5
        assert calculate_median([1, 2, 3, 4]) == 2.5

    def test_median_unsorted_input(self) -> None:
        """Test median with unsorted input."""
        assert calculate_median([5, 1, 3, 9, 7]) == 5.0

    def test_median_empty(self) -> None:
        """Test median of empty list."""
        assert calculate_median([]) == 0.0


class TestCalculateVariance:
    """Tests for calculate_variance function."""

    def test_population_variance(self) -> None:
        """Test population variance calculation."""
        values = [2, 4, 4, 4, 5, 5, 7, 9]
        # Population variance = 4.0
        assert abs(calculate_variance(values, population=True) - 4.0) < 0.001

    def test_sample_variance(self) -> None:
        """Test sample variance calculation."""
        values = [2, 4, 4, 4, 5, 5, 7, 9]
        # Sample variance = n/(n-1) * population_variance = 8/7 * 4 = 4.571...
        expected = 32 / 7  # ~4.571
        assert abs(calculate_variance(values, population=False) - expected) < 0.001

    def test_variance_single_value(self) -> None:
        """Test variance of single value list."""
        assert calculate_variance([5]) == 0.0


class TestCalculatePercentile:
    """Tests for calculate_percentile function."""

    def test_50th_percentile(self) -> None:
        """Test 50th percentile (should be close to median)."""
        values = list(range(1, 101))  # 1 to 100
        # 50th percentile should be around 50
        result = calculate_percentile(values, 50)
        assert 49 <= result <= 51

    def test_percentile_bounds(self) -> None:
        """Test percentile with boundary values."""
        values = [1, 2, 3, 4, 5]
        assert calculate_percentile(values, 0) == 1
        # 100th percentile should be the max value
        assert calculate_percentile(values, 100) == 5

    def test_invalid_percentile(self) -> None:
        """Test that invalid percentile raises error."""
        with pytest.raises(ValueError):
            calculate_percentile([1, 2, 3], 150)

    def test_negative_percentile(self) -> None:
        """Test that negative percentile raises error."""
        with pytest.raises(ValueError):
            calculate_percentile([1, 2, 3], -10)


class TestNormalizeValues:
    """Tests for normalize_values function."""

    def test_normalize_basic(self) -> None:
        """Test basic normalization."""
        result = normalize_values([0, 50, 100])
        assert result == [0.0, 0.5, 1.0]

    def test_normalize_empty(self) -> None:
        """Test normalizing empty list."""
        assert normalize_values([]) == []

    def test_normalize_same_values(self) -> None:
        """Test normalizing list with all same values - should not raise error."""
        # When all values are the same, normalization should return all 0.0 or handle gracefully
        result = normalize_values([5, 5, 5])
        assert result == [0.0, 0.0, 0.0]  # or could be [0.5, 0.5, 0.5] - just shouldn't crash


class TestCalculateCorrelation:
    """Tests for calculate_correlation function."""

    def test_perfect_positive_correlation(self) -> None:
        """Test perfectly correlated data."""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        assert abs(calculate_correlation(x, y) - 1.0) < 0.001

    def test_perfect_negative_correlation(self) -> None:
        """Test perfectly negatively correlated data."""
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        assert abs(calculate_correlation(x, y) - (-1.0)) < 0.001

    def test_correlation_length_mismatch(self) -> None:
        """Test that mismatched lengths raise error."""
        with pytest.raises(ValueError):
            calculate_correlation([1, 2, 3], [1, 2])

    def test_correlation_single_value(self) -> None:
        """Test correlation with single value - should handle gracefully."""
        # Single value means no variance, correlation undefined
        with pytest.raises((ValueError, ZeroDivisionError)):
            calculate_correlation([1], [2])

    def test_correlation_constant_values(self) -> None:
        """Test correlation when one list is constant - should handle gracefully."""
        # Constant list has zero std dev, correlation undefined
        with pytest.raises((ValueError, ZeroDivisionError)):
            calculate_correlation([1, 2, 3], [5, 5, 5])


class TestComputeStatistics:
    """Tests for compute_statistics function."""

    def test_compute_all_stats(self) -> None:
        """Test comprehensive statistics computation."""
        values = [1, 2, 3, 4, 5]
        result = compute_statistics(values)

        assert result.mean == 3.0
        assert result.median == 3.0
        assert result.min_val == 1.0
        assert result.max_val == 5.0
        assert result.count == 5

    def test_compute_empty_raises(self) -> None:
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError):
            compute_statistics([])

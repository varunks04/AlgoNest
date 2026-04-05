"""Tests for additional sorting algorithms."""

import pytest

from algonest import bucket_sort, cycle_sort, shell_sort, tim_sort


def test_advanced_sorts_return_sorted_output() -> None:
    data = [9, 3, 7, 1, 6]
    expected = [1, 3, 6, 7, 9]
    assert shell_sort(data) == expected
    assert cycle_sort(data) == expected
    assert tim_sort(data) == expected


def test_bucket_sort_handles_float_values() -> None:
    assert bucket_sort([0.42, 0.32, 0.23, 0.52, 0.25]) == [0.23, 0.25, 0.32, 0.42, 0.52]


def test_bucket_sort_raises_for_invalid_bucket_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        bucket_sort([1.0, 2.0], bucket_count=0)


def test_bucket_sort_raises_for_non_numeric_values() -> None:
    with pytest.raises(TypeError, match="numeric"):
        bucket_sort([1, "x", 3])

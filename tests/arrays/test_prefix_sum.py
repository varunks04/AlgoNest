"""Tests for prefix sum algorithms."""

import pytest

from algonest import prefix_sum, range_sum, subarray_sum_equals_k


def test_prefix_sum_happy_path() -> None:
    assert prefix_sum([3, 5, 2, 7]) == [3, 8, 10, 17]


def test_range_sum_happy_path() -> None:
    pref = prefix_sum([3, 5, 2, 7])
    assert range_sum(pref, 1, 3) == 14


def test_subarray_sum_equals_k_happy_path() -> None:
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2


def test_range_sum_raises_for_bad_indices() -> None:
    pref = prefix_sum([1, 2, 3])
    with pytest.raises(IndexError, match="valid indices"):
        range_sum(pref, 1, 10)

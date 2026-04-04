"""Tests for Kadane algorithm."""

import pytest

from algonest import max_subarray_sum


def test_max_subarray_sum_happy_path() -> None:
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_sum_single_value() -> None:
    assert max_subarray_sum([5]) == 5


def test_max_subarray_sum_raises_on_empty_input() -> None:
    with pytest.raises(ValueError, match="empty"):
        max_subarray_sum([])

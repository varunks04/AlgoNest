"""Tests for Dutch flag partition algorithms."""

from algonest import partition_by_pivot, sort_three_values


def test_sort_three_values_happy_path() -> None:
    assert sort_three_values([2, 0, 1, 2, 1, 0], 0, 1, 2) == [0, 0, 1, 1, 2, 2]


def test_partition_by_pivot_happy_path() -> None:
    assert partition_by_pivot([3, 5, 2, 5, 1], 3) == [2, 1, 3, 5, 5]

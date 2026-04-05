"""Tests for Phase 6 heap utilities."""

from algonest.heap import (
    MedianFinder,
    k_closest_points,
    kth_largest,
    kth_smallest,
    merge_k_sorted_arrays,
    top_k_frequent,
)


def test_k_element_helpers() -> None:
    assert kth_largest([3, 2, 1, 5], 2) == 3
    assert kth_smallest([3, 2, 1, 5], 2) == 2
    assert top_k_frequent([1, 1, 2, 3, 3, 3], 2) == [3, 1]


def test_median_finder() -> None:
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(3)
    assert mf.find_median() == 2.0


def test_merge_k_sorted_arrays_and_points() -> None:
    assert merge_k_sorted_arrays([[1, 4], [2, 3], [5]]) == [1, 2, 3, 4, 5]
    assert k_closest_points([(1, 3), (0, 1), (2, 2)], 2) == [(0, 1), (2, 2)]

"""Tests for interval helpers."""

from algonest import insert_interval, merge_intervals, non_overlapping_count


def test_merge_intervals_happy_path() -> None:
    assert merge_intervals([(1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]


def test_insert_interval_happy_path() -> None:
    intervals = [(1, 2), (3, 5), (6, 7), (8, 10)]
    assert insert_interval(intervals, (4, 9)) == [(1, 2), (3, 10)]


def test_non_overlapping_count() -> None:
    assert non_overlapping_count([(1, 2), (2, 3), (3, 4), (1, 3)]) == 1

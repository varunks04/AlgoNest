"""Tests for greedy utility package."""

from algonest.greedy import (
    can_reach_end,
    fractional_knapsack,
    max_non_overlapping_activities,
    min_jumps,
)


def test_activity_selection() -> None:
    intervals = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]
    selected = max_non_overlapping_activities(intervals)
    assert selected == [(1, 2), (3, 4), (5, 7), (8, 9)]


def test_fractional_knapsack() -> None:
    result = fractional_knapsack([10, 20, 30], [60, 100, 120], 50)
    assert result == 240.0


def test_jump_game_helpers() -> None:
    assert can_reach_end([2, 3, 1, 1, 4]) is True
    assert min_jumps([2, 3, 1, 1, 4]) == 2

"""Tests for monotonic stack algorithms."""

from algonest.stack_queue import largest_rectangle_in_histogram, next_greater_element


def test_next_greater_element_happy_path() -> None:
    assert next_greater_element([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]


def test_largest_rectangle_in_histogram_happy_path() -> None:
    assert largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]) == 10

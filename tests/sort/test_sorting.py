"""Tests for grouped sorting algorithms."""

import pytest

from algonest import (
    bubble_sort,
    counting_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    selection_sort,
)


def test_comparison_sorts_return_sorted_output() -> None:
    data = [3, 1, 2]
    expected = [1, 2, 3]
    assert bubble_sort(data) == expected
    assert selection_sort(data) == expected
    assert insertion_sort(data) == expected
    assert merge_sort(data) == expected
    assert quick_sort(data) == expected
    assert heap_sort(data) == expected


def test_counting_sort_handles_integers() -> None:
    assert counting_sort([4, 1, 3, 1]) == [1, 1, 3, 4]


def test_radix_sort_handles_non_negative_integers() -> None:
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2,
        24,
        45,
        66,
        75,
        90,
        170,
        802,
    ]


def test_counting_sort_raises_on_non_integer() -> None:
    with pytest.raises(TypeError, match="integer"):
        counting_sort([1, 2.5, 3])


def test_radix_sort_raises_on_negative_input() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        radix_sort([3, -1, 2])

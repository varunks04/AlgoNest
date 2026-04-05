"""Tests for reverse helpers."""

import pytest

from algonest import reverse_array, reverse_subarray, reverse_words


def test_reverse_array_happy_path() -> None:
    assert reverse_array([1, 2, 3]) == [3, 2, 1]


def test_reverse_subarray_happy_path() -> None:
    assert reverse_subarray([1, 2, 3, 4, 5], 1, 3) == [1, 4, 3, 2, 5]


def test_reverse_subarray_raises_on_invalid_range() -> None:
    with pytest.raises(IndexError, match="valid inclusive range"):
        reverse_subarray([1, 2, 3], 2, 1)


def test_reverse_words_normalizes_space() -> None:
    assert reverse_words("  alpha   beta gamma ") == "gamma beta alpha"

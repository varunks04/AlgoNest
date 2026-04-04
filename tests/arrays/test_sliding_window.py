"""Tests for grouped sliding window functions."""

import pytest

from algonest import longest_unique_substring, max_sum_subarray_k


def test_max_sum_subarray_k_happy_path() -> None:
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9


def test_max_sum_subarray_k_supports_tuple_and_numpy() -> None:
    assert max_sum_subarray_k((2, 1, 5, 1), 2) == 6
    np = pytest.importorskip("numpy")
    assert max_sum_subarray_k(np.array([2, 1, 5, 1]), 2) == 6


def test_max_sum_subarray_k_raises_value_error_for_invalid_window_size() -> None:
    with pytest.raises(ValueError, match="positive"):
        max_sum_subarray_k([1, 2, 3], 0)


def test_longest_unique_substring_happy_path() -> None:
    assert longest_unique_substring("abcabcbb") == 3


def test_longest_unique_substring_raises_type_error_for_non_string() -> None:
    with pytest.raises(TypeError, match="string"):
        longest_unique_substring(123)  # type: ignore[arg-type]

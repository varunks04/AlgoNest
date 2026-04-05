"""Tests for additional search algorithms."""

import pytest

from algonest import (
    binary_search_rotated,
    exponential_search,
    interpolation_search,
    search_2d_matrix,
    search_matrix_binary,
    search_matrix_staircase,
    search_rotated,
)


def test_binary_search_rotated_happy_path() -> None:
    data = [13, 18, 25, 2, 8, 10]
    assert binary_search_rotated(data, 8) == 4
    assert search_rotated(data, 2) == 3


def test_exponential_search_happy_path() -> None:
    assert exponential_search([1, 3, 5, 7, 9, 11], 7) == 3


def test_interpolation_search_happy_path() -> None:
    assert interpolation_search([10, 20, 30, 40, 50], 40) == 3


def test_interpolation_search_raises_on_non_numeric() -> None:
    with pytest.raises(TypeError, match="numeric"):
        interpolation_search(["a", "b"], "a")


def test_search_matrix_variants() -> None:
    matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
    ]
    assert search_matrix_staircase(matrix, 8) == (1, 2)

    row_major = [[1, 3, 5], [7, 9, 11]]
    assert search_matrix_binary(row_major, 9) == (1, 1)


def test_search_matrix_returns_negative_pair_when_missing() -> None:
    assert search_matrix_binary([[1, 2], [3, 4]], 10) == (-1, -1)


def test_search_2d_matrix_wrapper_supports_both_methods() -> None:
    staircase_matrix = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
    ]
    assert search_2d_matrix(staircase_matrix, 6, method="staircase") == (2, 1)

    row_major_matrix = [[1, 3, 5], [7, 9, 11]]
    assert search_2d_matrix(row_major_matrix, 9, method="binary") == (1, 1)


def test_search_2d_matrix_wrapper_rejects_invalid_method() -> None:
    with pytest.raises(ValueError, match="method"):
        search_2d_matrix([[1]], 1, method="unknown")

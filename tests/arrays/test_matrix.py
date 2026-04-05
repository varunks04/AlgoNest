"""Tests for matrix helpers."""

from algonest import diagonal_traversal, set_zeroes, transpose


def test_transpose_happy_path() -> None:
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_set_zeroes_happy_path() -> None:
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    assert set_zeroes(matrix) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_diagonal_traversal_happy_path() -> None:
    assert diagonal_traversal([[1, 2, 3], [4, 5, 6]]) == [1, 2, 4, 5, 3, 6]

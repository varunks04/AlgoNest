"""Tests for rotation utilities."""

from algonest import rotate_left, rotate_matrix_90, rotate_right, spiral_order


def test_rotate_left_and_right() -> None:
    data = [1, 2, 3, 4, 5]
    assert rotate_left(data, 2) == [3, 4, 5, 1, 2]
    assert rotate_right(data, 2) == [4, 5, 1, 2, 3]


def test_rotate_matrix_90() -> None:
    assert rotate_matrix_90([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]


def test_spiral_order() -> None:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

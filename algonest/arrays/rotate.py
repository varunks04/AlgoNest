"""Array rotation and traversal helpers."""

from typing import Iterable, List, TypeVar

from algonest.utils import _validate_iterable

ValueType = TypeVar("ValueType")


def rotate_left(arr: Iterable[ValueType], steps: int) -> List[ValueType]:
    """Return a new array rotated left by steps."""
    values: List[ValueType] = _validate_iterable(arr)
    if not values:
        return []
    shift = steps % len(values)
    return values[shift:] + values[:shift]


def rotate_right(arr: Iterable[ValueType], steps: int) -> List[ValueType]:
    """Return a new array rotated right by steps."""
    values: List[ValueType] = _validate_iterable(arr)
    if not values:
        return []
    shift = steps % len(values)
    return values[-shift:] + values[:-shift] if shift else values[:]


def rotate_matrix_90(matrix: Iterable[Iterable[ValueType]]) -> List[List[ValueType]]:
    """Return matrix rotated 90 degrees clockwise."""
    rows = [list(row) for row in _validate_iterable(matrix)]
    if not rows:
        return []
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise ValueError("matrix must be rectangular")
    return [
        [rows[row_index][col_index] for row_index in range(len(rows) - 1, -1, -1)]
        for col_index in range(width)
    ]


def spiral_order(matrix: Iterable[Iterable[ValueType]]) -> List[ValueType]:
    """Return matrix elements in spiral order."""
    rows = [list(row) for row in _validate_iterable(matrix)]
    if not rows:
        return []
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise ValueError("matrix must be rectangular")

    top = 0
    bottom = len(rows) - 1
    left = 0
    right = width - 1
    output: List[ValueType] = []

    while top <= bottom and left <= right:
        for col_index in range(left, right + 1):
            output.append(rows[top][col_index])
        top += 1

        for row_index in range(top, bottom + 1):
            output.append(rows[row_index][right])
        right -= 1

        if top <= bottom:
            for col_index in range(right, left - 1, -1):
                output.append(rows[bottom][col_index])
            bottom -= 1

        if left <= right:
            for row_index in range(bottom, top - 1, -1):
                output.append(rows[row_index][left])
            left += 1

    return output

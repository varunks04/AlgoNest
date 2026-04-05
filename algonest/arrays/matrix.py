"""2D array utility helpers."""

from typing import Iterable, List, TypeVar

from algonest.utils import _validate_iterable

ValueType = TypeVar("ValueType")


def _normalize_matrix(matrix: Iterable[Iterable[ValueType]]) -> List[List[ValueType]]:
    rows = [list(row) for row in _validate_iterable(matrix)]
    if not rows:
        return []

    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise ValueError("matrix must be rectangular")
    return rows


def transpose(matrix: Iterable[Iterable[ValueType]]) -> List[List[ValueType]]:
    """Return transposed matrix."""
    rows = _normalize_matrix(matrix)
    if not rows:
        return []
    return [list(col) for col in zip(*rows)]


def set_zeroes(matrix: Iterable[Iterable[int]]) -> List[List[int]]:
    """Return matrix where rows/cols containing 0 are set fully to 0."""
    rows = _normalize_matrix(matrix)
    if not rows:
        return []

    row_zeroes = set()
    col_zeroes = set()

    for r, row in enumerate(rows):
        for c, value in enumerate(row):
            if value == 0:
                row_zeroes.add(r)
                col_zeroes.add(c)

    result: List[List[int]] = []
    for r, row in enumerate(rows):
        result_row: List[int] = []
        for c, value in enumerate(row):
            if r in row_zeroes or c in col_zeroes:
                result_row.append(0)
            else:
                result_row.append(value)
        result.append(result_row)

    return result


def diagonal_traversal(matrix: Iterable[Iterable[ValueType]]) -> List[ValueType]:
    """Return zig-zag diagonal traversal of matrix."""
    rows = _normalize_matrix(matrix)
    if not rows:
        return []

    row_count = len(rows)
    n = len(rows[0])
    output: List[ValueType] = []

    for diagonal_index in range(row_count + n - 1):
        diagonal: List[ValueType] = []
        row_start = 0 if diagonal_index < n else diagonal_index - n + 1
        row_end = min(diagonal_index, row_count - 1)

        for row_index in range(row_start, row_end + 1):
            col_index = diagonal_index - row_index
            diagonal.append(rows[row_index][col_index])

        if diagonal_index % 2 == 0:
            output.extend(reversed(diagonal))
        else:
            output.extend(diagonal)

    return output

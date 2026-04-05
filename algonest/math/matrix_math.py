"""Basic matrix arithmetic helpers."""

from typing import List, Sequence


Matrix = List[List[int]]


def identity(size: int) -> Matrix:
    """Create an identity matrix of given size.

    Args:
        size: Matrix dimension.

    Returns:
        ``size x size`` identity matrix.

    Raises:
        ValueError: If ``size`` is negative.

    Time Complexity:
        O(size^2).

    Space Complexity:
        O(size^2).
    """
    if size < 0:
        raise ValueError("size must be non-negative")
    return [
        [1 if row_index == col_index else 0 for col_index in range(size)]
        for row_index in range(size)
    ]


def matrix_multiply(left: Sequence[Sequence[int]], right: Sequence[Sequence[int]]) -> Matrix:
    """Multiply two matrices.

    Args:
        left: Left matrix with shape ``r x k``.
        right: Right matrix with shape ``k x c``.

    Returns:
        Product matrix with shape ``r x c``.

    Raises:
        ValueError: If matrices are empty, ragged, or dimensions are incompatible.

    Time Complexity:
        O(r * k * c).

    Space Complexity:
        O(r * c).
    """
    if not left or not right or not left[0] or not right[0]:
        raise ValueError("matrices must be non-empty")

    left_rows = len(left)
    left_cols = len(left[0])
    right_rows = len(right)
    right_cols = len(right[0])

    for row in left:
        if len(row) != left_cols:
            raise ValueError("left matrix must be rectangular")
    for row in right:
        if len(row) != right_cols:
            raise ValueError("right matrix must be rectangular")

    if left_cols != right_rows:
        raise ValueError("left columns must match right rows")

    result = [[0] * right_cols for _ in range(left_rows)]

    for row_index in range(left_rows):
        for shared_index in range(left_cols):
            for col_index in range(right_cols):
                result[row_index][col_index] += (
                    left[row_index][shared_index] * right[shared_index][col_index]
                )

    return result


def matrix_power(matrix: Sequence[Sequence[int]], power: int) -> Matrix:
    """Raise a square matrix to a non-negative power.

    Args:
        matrix: Square matrix.
        power: Non-negative exponent.

    Returns:
        ``matrix`` raised to ``power``.

    Raises:
        ValueError: If ``power`` is negative or matrix is non-square/empty.

    Time Complexity:
        O(log power * n^3), where n is matrix dimension.

    Space Complexity:
        O(n^2).
    """
    if power < 0:
        raise ValueError("power must be non-negative")
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be non-empty and square")

    width = len(matrix[0])
    for row in matrix:
        if len(row) != width:
            raise ValueError("matrix must be rectangular")

    size = len(matrix)
    result = identity(size)
    base = [list(row) for row in matrix]
    exp = power

    while exp > 0:
        if exp & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exp >>= 1

    return result

"""Additional search algorithms for toolkit-style usage."""

from numbers import Real
from typing import Iterable, List, Tuple, TypeVar

from algonest.utils import _validate_iterable

ValueType = TypeVar("ValueType")


def binary_search_rotated(arr: Iterable[ValueType], target: ValueType) -> int:
    """Find a target in a rotated sorted array.

    Args:
        arr: Rotated sorted values with distinct comparable items.
        target: Value to find.

    Returns:
        Index of target, or ``-1`` when absent.

    Time Complexity:
        O(log n).

    Space Complexity:
        O(n) due to iterable normalization.
    """
    values: List[ValueType] = _validate_iterable(arr)
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if values[middle] == target:
            return middle

        if values[left] <= values[middle]:
            if values[left] <= target < values[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if values[middle] < target <= values[right]:
                left = middle + 1
            else:
                right = middle - 1

    return -1


def search_rotated(arr: Iterable[ValueType], target: ValueType) -> int:
    """Alias for :func:`binary_search_rotated`.

    Args:
        arr: Rotated sorted values.
        target: Value to locate.

    Returns:
        Target index, or ``-1``.

    Time Complexity:
        O(log n).

    Space Complexity:
        O(n).
    """
    return binary_search_rotated(arr, target)


def exponential_search(arr: Iterable[ValueType], target: ValueType) -> int:
    """Find a target in sorted data using exponential range expansion.

    Args:
        arr: Sorted comparable values.
        target: Value to locate.

    Returns:
        Index of target, or ``-1``.

    Time Complexity:
        O(log n).

    Space Complexity:
        O(n).
    """
    values: List[ValueType] = _validate_iterable(arr)
    if not values:
        return -1
    if values[0] == target:
        return 0

    bound = 1
    n = len(values)
    while bound < n and values[bound] < target:
        bound *= 2

    left = bound // 2
    right = min(bound, n - 1)

    while left <= right:
        middle = left + (right - left) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def interpolation_search(arr: Iterable[Real], target: Real) -> int:
    """Find a numeric target using interpolation search.

    Args:
        arr: Sorted numeric values.
        target: Numeric value to locate.

    Returns:
        Index of target, or ``-1`` if absent.

    Raises:
        TypeError: If target or array elements are non-numeric.

    Time Complexity:
        O(log log n) average, O(n) worst case.

    Space Complexity:
        O(n).
    """
    values = _validate_iterable(arr)
    if not values:
        return -1

    if isinstance(target, bool) or not isinstance(target, Real):
        raise TypeError("interpolation_search requires a numeric target")

    for value in values:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("interpolation_search requires numeric elements")

    left = 0
    right = len(values) - 1

    while left <= right and values[left] <= target <= values[right]:
        if values[left] == values[right]:
            return left if values[left] == target else -1

        probe_index = left + int(
            (float(target - values[left]) * (right - left))
            / float(values[right] - values[left])
        )

        if probe_index < left or probe_index > right:
            break

        if values[probe_index] == target:
            return probe_index
        if values[probe_index] < target:
            left = probe_index + 1
        else:
            right = probe_index - 1

    return -1


def search_matrix_staircase(
    matrix: Iterable[Iterable[ValueType]], target: ValueType
) -> Tuple[int, int]:
    """Search row/column sorted matrix using staircase walk.

    Args:
        matrix: Matrix sorted ascending across rows and columns.
        target: Value to locate.

    Returns:
        ``(row_index, col_index)`` or ``(-1, -1)``.

    Raises:
        ValueError: If matrix rows are not rectangular.

    Time Complexity:
        O(rows + cols).

    Space Complexity:
        O(rows * cols) from normalization.
    """
    rows = [list(row) for row in _validate_iterable(matrix)]
    if not rows:
        return (-1, -1)
    if not rows[0]:
        return (-1, -1)

    col_count = len(rows[0])
    for row in rows:
        if len(row) != col_count:
            raise ValueError("matrix must be rectangular")

    row_index = 0
    col_index = col_count - 1

    while row_index < len(rows) and col_index >= 0:
        value = rows[row_index][col_index]
        if value == target:
            return (row_index, col_index)
        if value > target:
            col_index -= 1
        else:
            row_index += 1

    return (-1, -1)


def search_matrix_binary(
    matrix: Iterable[Iterable[ValueType]], target: ValueType
) -> Tuple[int, int]:
    """Binary search in row-major sorted matrix.

    Args:
        matrix: Row-major sorted matrix.
        target: Value to locate.

    Returns:
        ``(row_index, col_index)`` or ``(-1, -1)``.

    Raises:
        ValueError: If matrix rows are not rectangular.

    Time Complexity:
        O(log(rows * cols)).

    Space Complexity:
        O(rows * cols) from normalization.
    """
    rows = [list(row) for row in _validate_iterable(matrix)]
    if not rows:
        return (-1, -1)
    if not rows[0]:
        return (-1, -1)

    col_count = len(rows[0])
    for row in rows:
        if len(row) != col_count:
            raise ValueError("matrix must be rectangular")

    left = 0
    right = len(rows) * col_count - 1

    while left <= right:
        middle = left + (right - left) // 2
        row_index = middle // col_count
        col_index = middle % col_count
        value = rows[row_index][col_index]

        if value == target:
            return (row_index, col_index)
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return (-1, -1)


def search_2d_matrix(
    matrix: Iterable[Iterable[ValueType]],
    target: ValueType,
    method: str = "staircase",
) -> Tuple[int, int]:
    """Search a 2D matrix using the requested strategy.

    Args:
        matrix: 2D matrix input.
        target: Value to locate.
        method: ``"staircase"`` or ``"binary"``.

    Returns:
        ``(row_index, col_index)`` when found, else ``(-1, -1)``.

    Raises:
        ValueError: If method is unsupported.

    Time Complexity:
        O(rows + cols) for staircase, O(log(rows * cols)) for binary.

    Space Complexity:
        O(rows * cols) from normalization.
    """
    if method == "staircase":
        return search_matrix_staircase(matrix, target)
    if method == "binary":
        return search_matrix_binary(matrix, target)
    raise ValueError("method must be either 'staircase' or 'binary'")

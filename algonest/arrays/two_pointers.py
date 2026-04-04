"""Two-pointer algorithms for array problems."""

from numbers import Real
from typing import Any, Iterable, Tuple

from algonest.utils import _validate_iterable


def two_sum_sorted(arr: Iterable[Real], target: Real) -> Tuple[int, int]:
    """Return indices of two values in sorted input whose sum equals target.

    Args:
        arr (Iterable[Real]): Sorted iterable of numeric values.
        target (Real): Desired sum.

    Returns:
        Tuple[int, int]: Pair of indices or (-1, -1) if not found.

    Raises:
        TypeError: If arr is not iterable or contains non-numeric values.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> two_sum_sorted([1, 2, 4, 7, 11], 9)
        (1, 3)
    """
    values = _validate_iterable(arr)
    if not isinstance(target, Real) or isinstance(target, bool):
        raise TypeError("target must be numeric")

    for value in values:
        if not isinstance(value, Real) or isinstance(value, bool):
            raise TypeError("All elements in arr must be numeric")

    left = 0
    right = len(values) - 1
    while left < right:
        current = values[left] + values[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return -1, -1


def remove_duplicates(arr: Iterable[Any]) -> int:
    """Return number of unique values in sorted iterable input.

    Args:
        arr (Iterable[Any]): Sorted iterable input values.

    Returns:
        int: Count of unique values.

    Raises:
        TypeError: If arr is not iterable.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> remove_duplicates([1, 1, 2, 2, 3])
        3
    """
    values = _validate_iterable(arr)
    if not values:
        return 0

    unique = 1
    for i in range(1, len(values)):
        if values[i] != values[i - 1]:
            unique += 1
    return unique


def container_with_water(arr: Iterable[Any]) -> int:
    """Return the maximum area formed by two lines and the x-axis.

    Args:
        arr (Iterable[Any]): Iterable of non-negative integer heights.

    Returns:
        int: Maximum container area.

    Raises:
        TypeError: If arr is not iterable or contains non-integer heights.
        ValueError: If any height is negative.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> container_with_water([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
    """
    values = _validate_iterable(arr)
    for value in values:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("All heights must be integers")
        if value < 0:
            raise ValueError("Heights must be non-negative")

    left = 0
    right = len(values) - 1
    best = 0
    while left < right:
        width = right - left
        area = width * min(values[left], values[right])
        if area > best:
            best = area
        if values[left] < values[right]:
            left += 1
        else:
            right -= 1
    return best

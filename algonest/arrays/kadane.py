"""Kadane algorithm for maximum subarray sum."""

from numbers import Real
from typing import Iterable

from algonest.utils import _validate_iterable


def max_subarray_sum(arr: Iterable[Real]) -> Real:
    """Return the maximum sum among all contiguous subarrays.

    Args:
        arr (Iterable[Real]): Iterable of numeric values.

    Returns:
        Real: Maximum contiguous subarray sum.

    Raises:
        TypeError: If arr is not iterable or contains non-numeric values.
        ValueError: If input is empty.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
    """
    values = _validate_iterable(arr)
    if not values:
        raise ValueError("arr cannot be empty")

    for value in values:
        if not isinstance(value, Real) or isinstance(value, bool):
            raise TypeError("All elements in arr must be numeric")

    current = values[0]
    best = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

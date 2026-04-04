"""Prefix-sum based array algorithms."""

from numbers import Real
from typing import Iterable, List

from algonest.utils import _validate_iterable


def prefix_sum(arr: Iterable[Real]) -> List[Real]:
    """Return prefix sums for numeric iterable input.

    Args:
        arr (Iterable[Real]): Iterable of numeric values.

    Returns:
        List[Real]: Prefix sums where out[i] = sum(arr[0:i+1]).

    Raises:
        TypeError: If arr is not iterable or contains non-numeric values.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> prefix_sum([3, 5, 2, 7])
        [3, 8, 10, 17]
    """
    values = _validate_iterable(arr)
    out: List[Real] = []
    running: Real = 0

    for value in values:
        if not isinstance(value, Real) or isinstance(value, bool):
            raise TypeError("All elements in arr must be numeric")
        running += value
        out.append(running)
    return out


def range_sum(prefix: Iterable[Real], left: int, right: int) -> Real:
    """Return inclusive sum from left to right using prefix sums.

    Args:
        prefix (Iterable[Real]): Prefix-sum iterable.
        left (int): Left index, inclusive.
        right (int): Right index, inclusive.

    Returns:
        Real: Sum over [left, right].

    Raises:
        TypeError: If prefix is not iterable or bounds are not integers.
        ValueError: If prefix is empty or left > right.
        IndexError: If bounds are out of range.

    Time Complexity: O(1)
    Space Complexity: O(n)

    Example:
        >>> p = prefix_sum([3, 5, 2, 7])
        >>> range_sum(p, 1, 3)
        14
    """
    values = _validate_iterable(prefix)
    if not values:
        raise ValueError("prefix cannot be empty")
    if not isinstance(left, int) or isinstance(left, bool):
        raise TypeError("left must be an integer")
    if not isinstance(right, int) or isinstance(right, bool):
        raise TypeError("right must be an integer")
    if left > right:
        raise ValueError("left cannot be greater than right")
    if left < 0 or right < 0 or left >= len(values) or right >= len(values):
        raise IndexError("left and right must be valid indices")

    return values[right] if left == 0 else values[right] - values[left - 1]


def subarray_sum_equals_k(arr: Iterable[Real], k: Real) -> int:
    """Return count of contiguous subarrays with sum exactly equal to k.

    Args:
        arr (Iterable[Real]): Iterable of numeric values.
        k (Real): Target sum.

    Returns:
        int: Number of matching subarrays.

    Raises:
        TypeError: If arr is not iterable or contains non-numeric values.
        TypeError: If k is not numeric.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> subarray_sum_equals_k([1, 1, 1], 2)
        2
    """
    values = _validate_iterable(arr)
    if not isinstance(k, Real) or isinstance(k, bool):
        raise TypeError("k must be numeric")

    for value in values:
        if not isinstance(value, Real) or isinstance(value, bool):
            raise TypeError("All elements in arr must be numeric")

    count = 0
    running: Real = 0
    seen = {0: 1}
    for value in values:
        running += value
        count += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1
    return count

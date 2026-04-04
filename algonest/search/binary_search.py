"""Grouped binary-search-family algorithms."""

from typing import Any, Iterable, List, TypeVar

from algonest.utils import _validate_iterable

T = TypeVar("T")


def linear_search(arr: Iterable[T], target: T) -> int:
    """Return index of target using sequential scan.

    Args:
        arr (Iterable[T]): Iterable input data.
        target (T): Value to locate.

    Returns:
        int: Index when found, otherwise -1.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n)
    Space Complexity: O(n) due to list conversion

    Example:
        >>> linear_search([4, 2, 7], 7)
        2
    """
    values: List[Any] = _validate_iterable(arr)
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def lower_bound(arr: Iterable[T], target: T) -> int:
    """Return the first index whose value is greater than or equal to target.

    Args:
        arr (Iterable[T]): Sorted iterable input.
        target (T): Boundary target value.

    Returns:
        int: First index i where values[i] >= target, or len(values).

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(log n)
    Space Complexity: O(n) due to list conversion

    Example:
        >>> lower_bound([1, 2, 2, 4], 2)
        1
    """
    values: List[Any] = _validate_iterable(arr)
    left = 0
    right = len(values)

    while left < right:
        middle = left + (right - left) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle

    return left


def upper_bound(arr: Iterable[T], target: T) -> int:
    """Return the first index whose value is strictly greater than target.

    Args:
        arr (Iterable[T]): Sorted iterable input.
        target (T): Boundary target value.

    Returns:
        int: First index i where values[i] > target, or len(values).

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(log n)
    Space Complexity: O(n) due to list conversion

    Example:
        >>> upper_bound([1, 2, 2, 4], 2)
        3
    """
    values: List[Any] = _validate_iterable(arr)
    left = 0
    right = len(values)

    while left < right:
        middle = left + (right - left) // 2
        if values[middle] <= target:
            left = middle + 1
        else:
            right = middle

    return left


def binary_search(arr: Iterable[T], target: T) -> int:
    """Return the index of target in sorted data, or -1 if not found.

    Args:
        arr (Iterable[T]): Sorted iterable input.
        target (T): Value to locate.

    Returns:
        int: Index of target when found, otherwise -1.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(log n)
    Space Complexity: O(n) due to list conversion

    Example:
        >>> binary_search([1, 3, 5, 7], 5)
        2
    """
    values: List[Any] = _validate_iterable(arr)
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def ternary_search(arr: Iterable[T], target: T) -> int:
    """Return index of target using iterative ternary search.

    Args:
        arr (Iterable[T]): Sorted iterable input.
        target (T): Value to locate.

    Returns:
        int: Index when found, otherwise -1.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(log_3 n)
    Space Complexity: O(n) due to list conversion

    Example:
        >>> ternary_search([1, 3, 5, 7, 9], 5)
        2
    """
    values: List[Any] = _validate_iterable(arr)
    left = 0
    right = len(values) - 1

    while left <= right:
        third = (right - left) // 3
        middle1 = left + third
        middle2 = right - third
        if values[middle1] == target:
            return middle1
        if values[middle2] == target:
            return middle2
        if target < values[middle1]:
            right = middle1 - 1
        elif target > values[middle2]:
            left = middle2 + 1
        else:
            left = middle1 + 1
            right = middle2 - 1

    return -1


def jump_search(arr: Iterable[T], target: T) -> int:
    """Return index of target using jump search.

    Args:
        arr (Iterable[T]): Sorted iterable input.
        target (T): Value to locate.

    Returns:
        int: Index when found, otherwise -1.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(sqrt(n))
    Space Complexity: O(n) due to list conversion

    Example:
        >>> jump_search([1, 3, 5, 7, 9], 7)
        3
    """
    values: List[Any] = _validate_iterable(arr)
    n = len(values)
    if n == 0:
        return -1

    step = int(n**0.5)
    prev = 0

    while prev < n and values[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1

    while prev < min(step, n):
        if values[prev] == target:
            return prev
        prev += 1

    return -1

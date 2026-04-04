"""Sliding window algorithms."""

from numbers import Real
from typing import Iterable

from algonest.utils import _validate_iterable


def max_sum_subarray_k(arr: Iterable[Real], k: int) -> Real:
    """Return maximum sum over all contiguous subarrays of size k.

    Args:
        arr (Iterable[Real]): Iterable numeric input.
        k (int): Window size.

    Returns:
        Real: Maximum subarray sum of length k.

    Raises:
        TypeError: If arr is not an iterable.
        TypeError: If array values are not numeric.
        ValueError: If k is not a valid positive integer in bounds.

    Time Complexity: O(n)
    Space Complexity: O(n) due to list conversion

    Example:
        >>> max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3)
        9
    """
    values = _validate_iterable(arr)

    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k must be an integer")
    if k <= 0:
        raise ValueError("k must be a positive integer")
    if k > len(values):
        raise ValueError("k cannot be greater than the length of input")

    for element in values:
        if not isinstance(element, Real) or isinstance(element, bool):
            raise TypeError("All elements in arr must be numeric")

    window_sum = sum(values[:k])
    best_sum = window_sum

    for right in range(k, len(values)):
        window_sum += values[right]
        window_sum -= values[right - k]
        if window_sum > best_sum:
            best_sum = window_sum

    return best_sum


def longest_unique_substring(s: str) -> int:
    """Return length of the longest substring without repeated characters.

    Args:
        s (str): Input string.

    Returns:
        int: Longest unique substring length.

    Raises:
        TypeError: If s is not a string.

    Time Complexity: O(n)
    Space Complexity: O(min(n, alphabet_size))

    Example:
        >>> longest_unique_substring("abcabcbb")
        3
    """
    if not isinstance(s, str):
        raise TypeError("longest_unique_substring expects 's' to be a string")

    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length

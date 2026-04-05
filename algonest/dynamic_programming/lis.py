"""Longest increasing subsequence algorithm."""

from typing import List, Sequence


def lis_length(values: Sequence[int]) -> int:
    """Compute LIS length using patience sorting with binary search.

    Args:
        values: Input sequence.

    Returns:
        Length of the longest strictly increasing subsequence.

    Time Complexity:
        O(n log n).

    Space Complexity:
        O(n).
    """
    if not values:
        return 0

    tails: List[int] = []
    for value in values:
        left = 0
        right = len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < value:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(value)
        else:
            tails[left] = value

    return int(len(tails))

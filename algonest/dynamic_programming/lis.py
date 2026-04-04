"""Longest increasing subsequence algorithm."""

from typing import List


def lis_length(values: List[int]) -> int:
    """Return LIS length using O(n log n) patience approach."""
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

    return len(tails)

"""Subset-partition style DP helpers."""

from typing import Iterable, List


def subset_sum(values: Iterable[int], target: int) -> bool:
    """Check whether any subset sums exactly to the target.

    Args:
        values: Candidate integers.
        target: Desired sum.

    Returns:
        ``True`` when a subset matches ``target``, else ``False``.

    Raises:
        ValueError: If any input value is negative.

    Time Complexity:
        O(len(values) * target).

    Space Complexity:
        O(target).
    """
    nums = list(values)
    if target < 0:
        return False
    if any(num < 0 for num in nums):
        raise ValueError("subset_sum expects non-negative input values")

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for current in range(target, num - 1, -1):
            dp[current] = dp[current] or dp[current - num]

    return bool(dp[target])


def partition_equal_subset(values: Iterable[int]) -> bool:
    """Check whether values can be partitioned into two equal-sum subsets.

    Args:
        values: Candidate integers.

    Returns:
        ``True`` if the sequence can be split into two equal-sum subsets.

    Raises:
        ValueError: If any input value is negative.

    Time Complexity:
        O(len(values) * total_sum).

    Space Complexity:
        O(total_sum).
    """
    nums: List[int] = list(values)
    if any(num < 0 for num in nums):
        raise ValueError("partition_equal_subset expects non-negative input values")
    total = sum(nums)
    if total % 2 != 0:
        return False
    return subset_sum(nums, total // 2)

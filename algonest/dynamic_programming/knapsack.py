"""Knapsack dynamic programming algorithms."""

from typing import List


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """Return maximum value for 0/1 knapsack."""
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for c in range(capacity, weights[i] - 1, -1):
            dp[c] = max(dp[c], values[i] + dp[c - weights[i]])
    return dp[capacity]


def unbounded_knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """Return maximum value for unbounded knapsack."""
    dp = [0] * (capacity + 1)
    for c in range(capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= c:
                dp[c] = max(dp[c], values[i] + dp[c - weights[i]])
    return dp[capacity]

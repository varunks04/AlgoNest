"""Knapsack dynamic programming algorithms."""

from typing import Sequence


def knapsack_01(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """Solve the 0/1 knapsack problem.

    Args:
        weights: Item weights, each positive.
        values: Item values aligned with ``weights``.
        capacity: Maximum carrying capacity.

    Returns:
        Maximum achievable value with each item used at most once.

    Raises:
        ValueError: If lengths mismatch, capacity is negative, or any weight is
            non-positive.

    Time Complexity:
        O(n * capacity).

    Space Complexity:
        O(capacity).
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if any(weight <= 0 for weight in weights):
        raise ValueError("weights must contain only positive values")

    item_count = len(weights)
    dp = [0] * (capacity + 1)
    for index in range(item_count):
        weight = weights[index]
        value = values[index]
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                value + dp[current_capacity - weight],
            )
    return int(dp[capacity])


def unbounded_knapsack(
    weights: Sequence[int], values: Sequence[int], capacity: int
) -> int:
    """Solve the unbounded knapsack problem.

    Args:
        weights: Item weights, each positive.
        values: Item values aligned with ``weights``.
        capacity: Maximum carrying capacity.

    Returns:
        Maximum achievable value with unlimited item reuse.

    Raises:
        ValueError: If lengths mismatch, capacity is negative, or any weight is
            non-positive.

    Time Complexity:
        O(n * capacity).

    Space Complexity:
        O(capacity).
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if any(weight <= 0 for weight in weights):
        raise ValueError("weights must contain only positive values")

    dp = [0] * (capacity + 1)
    for current_capacity in range(capacity + 1):
        for index in range(len(weights)):
            weight = weights[index]
            if weight <= current_capacity:
                dp[current_capacity] = max(
                    dp[current_capacity],
                    values[index] + dp[current_capacity - weight],
                )
    return int(dp[capacity])

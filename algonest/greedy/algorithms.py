"""Greedy algorithms that are commonly reused as toolkit primitives.

This module intentionally groups lightweight greedy helpers so the package
structure remains practical instead of overly fragmented.
"""

from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple

Interval = Tuple[int, int]


def max_non_overlapping_activities(intervals: Iterable[Sequence[int]]) -> List[Interval]:
    """Select a maximum-size set of non-overlapping intervals.

    Args:
        intervals: Iterable of 2-item sequences ``(start, end)``.

    Returns:
        A list of selected intervals sorted by finishing time.

    Raises:
        ValueError: If any interval is malformed or has ``start > end``.

    Time Complexity:
        O(n log n) due to sorting.

    Space Complexity:
        O(n) for normalized/sorted intervals and output.
    """
    normalized: List[Interval] = []
    for interval in intervals:
        if len(interval) != 2:
            raise ValueError("each interval must contain exactly two values")
        start, end = int(interval[0]), int(interval[1])
        if start > end:
            raise ValueError("interval start must be <= interval end")
        normalized.append((start, end))

    normalized.sort(key=lambda pair: pair[1])
    selected: List[Interval] = []
    latest_end = float("-inf")

    for start, end in normalized:
        if start >= latest_end:
            selected.append((start, end))
            latest_end = end

    return selected


def fractional_knapsack(
    weights: Sequence[float], values: Sequence[float], capacity: float
) -> float:
    """Compute maximum value with fractional item selection.

    Args:
        weights: Item weights, each value must be positive.
        values: Item values aligned with ``weights``.
        capacity: Total knapsack capacity.

    Returns:
        Maximum achievable value as a float.

    Raises:
        ValueError: If lengths mismatch, capacity is negative, or any weight is
            non-positive.

    Time Complexity:
        O(n log n) due to sorting by value density.

    Space Complexity:
        O(n) for item tuples.
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")

    items: List[Tuple[float, float, float]] = []
    for weight, value in zip(weights, values):
        if weight <= 0:
            raise ValueError("weights must be positive")
        items.append((value / weight, weight, value))

    items.sort(reverse=True)
    remaining = float(capacity)
    best_value = 0.0

    for ratio, weight, value in items:
        if remaining <= 0:
            break
        if weight <= remaining:
            best_value += value
            remaining -= weight
        else:
            best_value += ratio * remaining
            break

    return best_value


def can_reach_end(values: Sequence[int]) -> bool:
    """Return whether the last index is reachable in Jump Game.

    Args:
        values: Non-negative jump lengths at each index.

    Returns:
        ``True`` if index ``len(values)-1`` is reachable, else ``False``.

    Raises:
        ValueError: If any jump length is negative.

    Time Complexity:
        O(n).

    Space Complexity:
        O(1).
    """
    farthest_reach = 0
    for index, jump in enumerate(values):
        if jump < 0:
            raise ValueError("jump lengths must be non-negative")
        if index > farthest_reach:
            return False
        farthest_reach = max(farthest_reach, index + jump)
        if farthest_reach >= len(values) - 1:
            return True
    return True


def min_jumps(values: Sequence[int]) -> int:
    """Return the minimum jumps needed to reach the last index.

    Args:
        values: Non-negative jump lengths at each index.

    Returns:
        Minimum jumps required, or ``-1`` if the end is unreachable.

    Raises:
        ValueError: If any jump length is negative.

    Time Complexity:
        O(n).

    Space Complexity:
        O(1).
    """
    if len(values) <= 1:
        return 0

    for jump in values:
        if jump < 0:
            raise ValueError("jump lengths must be non-negative")

    if values[0] == 0:
        return -1

    jump_count = 0
    current_window_end = 0
    farthest_reach = 0

    for index in range(len(values) - 1):
        farthest_reach = max(farthest_reach, index + values[index])
        if index == current_window_end:
            jump_count += 1
            current_window_end = farthest_reach
            if current_window_end >= len(values) - 1:
                return jump_count

    return -1

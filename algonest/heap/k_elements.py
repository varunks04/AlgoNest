"""Heap-based selection utilities."""

import heapq
from collections import Counter
from typing import Iterable, List, Sequence, Tuple


def kth_largest(values: Iterable[int], k: int) -> int:
    """Return kth largest value."""
    data = list(values)
    if k <= 0 or k > len(data):
        raise IndexError("k must be in range [1, len(values)]")
    return heapq.nlargest(k, data)[-1]


def kth_smallest(values: Iterable[int], k: int) -> int:
    """Return kth smallest value."""
    data = list(values)
    if k <= 0 or k > len(data):
        raise IndexError("k must be in range [1, len(values)]")
    return heapq.nsmallest(k, data)[-1]


def top_k_frequent(values: Iterable[int], k: int) -> List[int]:
    """Return elements with top-k frequencies."""
    counts = Counter(values)
    if k <= 0:
        return []
    return [value for value, _ in counts.most_common(k)]


def k_closest_points(points: Sequence[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    """Return k points closest to origin."""
    if k <= 0:
        return []
    ranked = sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])
    return ranked[:k]

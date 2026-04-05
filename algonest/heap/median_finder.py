"""Streaming median finder with two heaps."""

import heapq
from typing import List


class MedianFinder:
    """Maintain running median in O(log n) insertion."""

    def __init__(self) -> None:
        self._low: List[int] = []
        self._high: List[int] = []

    def add_num(self, value: int) -> None:
        if not self._low or value <= -self._low[0]:
            heapq.heappush(self._low, -value)
        else:
            heapq.heappush(self._high, value)

        if len(self._low) > len(self._high) + 1:
            heapq.heappush(self._high, -heapq.heappop(self._low))
        elif len(self._high) > len(self._low):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def find_median(self) -> float:
        if not self._low and not self._high:
            raise ValueError("no elements present")
        if len(self._low) == len(self._high):
            return (-self._low[0] + self._high[0]) / 2.0
        return float(-self._low[0])

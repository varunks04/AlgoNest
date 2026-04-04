"""Fenwick tree (Binary Indexed Tree) implementation."""

from typing import List


class FenwickTree:
    """Support prefix sums and point updates in logarithmic time."""

    def __init__(self, size: int) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")
        self.size = size
        self.tree = [0] * (size + 1)

    def point_update(self, index: int, delta: int) -> None:
        """Add delta to value at zero-based index."""
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        i = index + 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def prefix_sum(self, index: int) -> int:
        """Return sum from index 0 to index inclusive."""
        if index < 0:
            return 0
        if index >= self.size:
            raise IndexError("index out of range")
        total = 0
        i = index + 1
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_query(self, left: int, right: int) -> int:
        """Return inclusive sum on range [left, right]."""
        if left > right:
            raise ValueError("left cannot be greater than right")
        if left < 0 or right >= self.size:
            raise IndexError("range out of bounds")
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

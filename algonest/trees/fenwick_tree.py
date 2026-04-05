"""Fenwick tree (Binary Indexed Tree) implementation."""


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
        tree_index = index + 1
        while tree_index <= self.size:
            self.tree[tree_index] += delta
            tree_index += tree_index & -tree_index

    def prefix_sum(self, index: int) -> int:
        """Return sum from index 0 to index inclusive."""
        if index < 0:
            return 0
        if index >= self.size:
            raise IndexError("index out of range")
        total = 0
        tree_index = index + 1
        while tree_index > 0:
            total += self.tree[tree_index]
            tree_index -= tree_index & -tree_index
        return total

    def range_query(self, left: int, right: int) -> int:
        """Return inclusive sum on range [left, right]."""
        if left > right:
            raise ValueError("left cannot be greater than right")
        if left < 0 or right >= self.size:
            raise IndexError("range out of bounds")
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

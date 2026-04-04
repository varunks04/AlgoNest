"""Disjoint Set Union (Union-Find) implementation."""

from typing import List


class DSU:
    """Support union-find operations with path compression and rank."""

    def __init__(self, size: int) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")
        self.parent: List[int] = list(range(size))
        self.rank: List[int] = [0] * size

    def find(self, x: int) -> int:
        """Return representative of x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """Union sets of a and b; return True when merged."""
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

"""Kruskal minimum spanning tree algorithm."""

from typing import List, Tuple

from algonest.graphs.dsu import DSU


def kruskal_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> int:
    """Return total weight of minimum spanning tree."""
    dsu = DSU(vertices)
    total = 0
    used = 0

    for u, v, w in sorted(edges, key=lambda edge: edge[2]):
        if dsu.union(u, v):
            total += w
            used += 1
            if used == vertices - 1:
                break

    return total

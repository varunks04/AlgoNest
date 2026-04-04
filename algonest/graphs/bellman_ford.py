"""Bellman-Ford shortest-path algorithm."""

from typing import List, Tuple


def bellman_ford(
    vertices: int,
    edges: List[Tuple[int, int, int]],
    source: int,
) -> Tuple[List[int], bool]:
    """Return shortest distances and negative-cycle detection flag."""
    dist = [10**18] * vertices
    dist[source] = 0

    for _ in range(vertices - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != 10**18 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != 10**18 and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, has_negative_cycle

"""Dijkstra shortest-path algorithm."""

import heapq
from typing import Dict, List, Tuple


def dijkstra_shortest_paths(
    graph: Dict[int, List[Tuple[int, int]]],
    source: int,
) -> Dict[int, int]:
    """Return shortest distances from source in non-negative weighted graph."""
    distances = {node: 10**18 for node in graph}
    if source not in graph:
        return distances

    distances[source] = 0
    heap: List[Tuple[int, int]] = [(0, source)]

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for nxt, weight in graph.get(node, []):
            candidate = dist + weight
            if candidate < distances[nxt]:
                distances[nxt] = candidate
                heapq.heappush(heap, (candidate, nxt))

    return distances

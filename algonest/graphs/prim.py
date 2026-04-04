"""Prim minimum spanning tree algorithm."""

import heapq
from typing import Dict, List, Set, Tuple


def prim_mst(graph: Dict[int, List[Tuple[int, int]]], start: int = 0) -> int:
    """Return total weight of MST for connected weighted graph."""
    if start not in graph:
        return 0

    visited: Set[int] = {start}
    heap: List[Tuple[int, int]] = []
    for nxt, weight in graph[start]:
        heapq.heappush(heap, (weight, nxt))

    total = 0
    while heap:
        weight, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        total += weight
        for nxt, edge_weight in graph.get(node, []):
            if nxt not in visited:
                heapq.heappush(heap, (edge_weight, nxt))

    return total

"""Breadth-first search graph algorithms."""

from collections import deque
from typing import Deque, Dict, List, Optional


def bfs_traversal(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return BFS traversal order from start node."""
    if start not in graph:
        return []
    visited = {start}
    order: List[int] = []
    queue: Deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    return order


def shortest_path_unweighted(
    graph: Dict[int, List[int]], start: int, target: int
) -> Optional[List[int]]:
    """Return shortest path in unweighted graph using BFS."""
    if start not in graph or target not in graph:
        return None

    queue: Deque[int] = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node == target:
            break
        for nxt in graph.get(node, []):
            if nxt not in parent:
                parent[nxt] = node
                queue.append(nxt)

    if target not in parent:
        return None

    path: List[int] = []
    node: Optional[int] = target
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]

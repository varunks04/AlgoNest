"""Topological sort algorithms."""

from collections import deque
from typing import Deque, Dict, List, Set


def kahn_topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    """Return topological ordering using Kahn algorithm."""
    indegree = {node: 0 for node in graph}
    for node, neighbors in graph.items():
        for nxt in neighbors:
            if nxt not in indegree:
                indegree[nxt] = 0
            indegree[nxt] += 1

    queue: Deque[int] = deque([n for n, deg in indegree.items() if deg == 0])
    order: List[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order


def dfs_topological_sort(graph: Dict[int, List[int]]) -> List[int]:
    """Return topological ordering using DFS postorder."""
    visited: Set[int] = set()
    temp: Set[int] = set()
    order: List[int] = []

    def _dfs(node: int) -> None:
        if node in temp:
            raise ValueError("graph is not a DAG")
        if node in visited:
            return
        temp.add(node)
        for nxt in graph.get(node, []):
            _dfs(nxt)
        temp.remove(node)
        visited.add(node)
        order.append(node)

    for node in graph:
        if node not in visited:
            _dfs(node)

    return order[::-1]

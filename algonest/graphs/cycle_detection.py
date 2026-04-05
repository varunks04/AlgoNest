"""Cycle detection helpers for directed/undirected graphs."""

from typing import Dict, List, Set


def has_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """Return whether undirected graph contains a cycle."""
    visited: Set[int] = set()

    def _dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                if _dfs(nxt, node):
                    return True
            elif nxt != parent:
                return True
        return False

    for node in graph:
        if node not in visited and _dfs(node, -1):
            return True
    return False


def has_cycle_directed(graph: Dict[int, List[int]]) -> bool:
    """Return whether directed graph contains a cycle."""
    visiting: Set[int] = set()
    visited: Set[int] = set()

    def _dfs(node: int) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False

        visiting.add(node)
        for nxt in graph.get(node, []):
            if _dfs(nxt):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    for node in graph:
        if _dfs(node):
            return True
    return False

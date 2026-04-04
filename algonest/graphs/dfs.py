"""Depth-first search graph algorithms."""

from typing import Dict, List, Set


def dfs_traversal(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return DFS traversal order from start node."""
    if start not in graph:
        return []

    visited: Set[int] = set()
    order: List[int] = []

    def _dfs(node: int) -> None:
        visited.add(node)
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                _dfs(nxt)

    _dfs(start)
    return order


def connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Return list of connected components for undirected graph."""
    visited: Set[int] = set()
    components: List[List[int]] = []

    for node in graph:
        if node in visited:
            continue
        comp: List[int] = []

        def _dfs(cur: int) -> None:
            visited.add(cur)
            comp.append(cur)
            for nxt in graph.get(cur, []):
                if nxt not in visited:
                    _dfs(nxt)

        _dfs(node)
        components.append(comp)

    return components


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

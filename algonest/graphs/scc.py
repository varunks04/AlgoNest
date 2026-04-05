"""Strongly connected components algorithms."""

from typing import Dict, List, Set


def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Return SCCs using Kosaraju's algorithm."""
    visited: Set[int] = set()
    order: List[int] = []

    def _dfs(node: int) -> None:
        visited.add(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                _dfs(nxt)
        order.append(node)

    for node in graph:
        if node not in visited:
            _dfs(node)

    reverse: Dict[int, List[int]] = {node: [] for node in graph}
    for source_node, neighbors in graph.items():
        for target_node in neighbors:
            reverse.setdefault(target_node, []).append(source_node)

    visited.clear()
    components: List[List[int]] = []

    def _dfs_reverse(node: int, comp: List[int]) -> None:
        visited.add(node)
        comp.append(node)
        for nxt in reverse.get(node, []):
            if nxt not in visited:
                _dfs_reverse(nxt, comp)

    for node in reversed(order):
        if node not in visited:
            comp: List[int] = []
            _dfs_reverse(node, comp)
            components.append(comp)

    return components

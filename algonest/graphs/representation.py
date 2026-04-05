"""Graph representation conversion helpers."""

from typing import Dict, Iterable, List, Sequence, Tuple


def edge_list_to_adj(
    edges: Iterable[Tuple[int, int]], directed: bool = False
) -> Dict[int, List[int]]:
    """Convert an edge list to adjacency-list representation.

    Args:
        edges: Iterable of ``(source, target)`` edges.
        directed: Whether the graph is directed.

    Returns:
        Adjacency list dictionary.

    Time Complexity:
        O(E).

    Space Complexity:
        O(V + E).
    """
    adj: Dict[int, List[int]] = {}
    for source_node, target_node in edges:
        adj.setdefault(source_node, []).append(target_node)
        adj.setdefault(target_node, [])
        if not directed:
            adj[target_node].append(source_node)
    return adj


def adj_list_to_matrix(adj: Dict[int, List[int]]) -> List[List[int]]:
    """Convert adjacency list to adjacency matrix.

    Args:
        adj: Adjacency-list graph.

    Returns:
        Adjacency matrix ordered by sorted node ids.

    Time Complexity:
        O(V^2 + E).

    Space Complexity:
        O(V^2).
    """
    nodes = sorted(adj.keys())
    node_to_index = {node: index for index, node in enumerate(nodes)}
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]

    for source_node, neighbors in adj.items():
        for target_node in neighbors:
            matrix[node_to_index[source_node]][node_to_index[target_node]] = 1

    return matrix


def matrix_to_adj_list(matrix: Sequence[Sequence[int]]) -> Dict[int, List[int]]:
    """Convert adjacency matrix to adjacency list using 0..n-1 indices."""
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be square")

    adj: Dict[int, List[int]] = {node_index: [] for node_index in range(n)}
    for source_index in range(n):
        for target_index in range(n):
            if matrix[source_index][target_index] != 0:
                adj[source_index].append(target_index)
    return adj

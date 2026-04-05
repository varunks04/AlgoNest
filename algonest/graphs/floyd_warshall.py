"""Floyd-Warshall all-pairs shortest-path algorithm."""

from typing import List


def floyd_warshall(matrix: List[List[int]]) -> List[List[int]]:
    """Compute all-pairs shortest paths using Floyd-Warshall.

    Args:
        matrix: Adjacency matrix with edge weights.

    Returns:
        Matrix of minimum path costs between all pairs.

    Time Complexity:
        O(n^3).

    Space Complexity:
        O(n^2).
    """
    n = len(matrix)
    dist = [row[:] for row in matrix]

    for intermediate_node in range(n):
        for source_node in range(n):
            for target_node in range(n):
                if (
                    dist[source_node][intermediate_node]
                    + dist[intermediate_node][target_node]
                    < dist[source_node][target_node]
                ):
                    dist[source_node][target_node] = (
                        dist[source_node][intermediate_node]
                        + dist[intermediate_node][target_node]
                    )

    return dist

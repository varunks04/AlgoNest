"""Bipartite graph check."""

from collections import deque
from typing import Deque, Dict, List


def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """Return whether graph is bipartite."""
    color: Dict[int, int] = {}

    for start in graph:
        if start in color:
            continue

        queue: Deque[int] = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for nxt in graph.get(node, []):
                if nxt not in color:
                    color[nxt] = 1 - color[node]
                    queue.append(nxt)
                elif color[nxt] == color[node]:
                    return False

    return True

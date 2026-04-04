from algonest.graphs import bfs_traversal, shortest_path_unweighted


def test_bfs_and_shortest_path() -> None:
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert bfs_traversal(graph, 0) == [0, 1, 2, 3]
    assert shortest_path_unweighted(graph, 0, 3) in ([0, 1, 3], [0, 2, 3])

from algonest.graphs import dijkstra_shortest_paths


def test_dijkstra() -> None:
    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    dist = dijkstra_shortest_paths(graph, 0)
    assert dist[3] == 4

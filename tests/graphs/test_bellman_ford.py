from algonest.graphs import bellman_ford


def test_bellman_ford() -> None:
    edges = [(0, 1, 5), (1, 2, 3), (0, 2, 10)]
    dist, has_neg = bellman_ford(3, edges, 0)
    assert dist[2] == 8
    assert has_neg is False

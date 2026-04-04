from algonest.graphs import kruskal_mst


def test_kruskal() -> None:
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    assert kruskal_mst(4, edges) == 19

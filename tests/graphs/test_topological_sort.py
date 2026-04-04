from algonest.graphs import dfs_topological_sort, kahn_topological_sort


def test_topological_sorts() -> None:
    graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 1: [], 0: []}
    assert set(kahn_topological_sort(dict(graph))) == set(graph.keys())
    assert set(dfs_topological_sort(graph)) == set(graph.keys())

from algonest.graphs import connected_components, dfs_traversal, has_cycle_undirected


def test_dfs_components_cycle() -> None:
    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert dfs_traversal({0: [1], 1: []}, 0) == [0, 1]
    assert len(connected_components(graph)) == 2
    assert has_cycle_undirected({0: [1], 1: [0, 2], 2: [1, 0]}) is True

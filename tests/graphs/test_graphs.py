"""Consolidated tests for graph utilities."""

from algonest.graphs import (
    DSU,
    adj_list_to_matrix,
    bellman_ford,
    bfs_traversal,
    connected_components,
    dfs_topological_sort,
    dfs_traversal,
    dijkstra_shortest_paths,
    edge_list_to_adj,
    floyd_warshall,
    has_cycle_directed,
    has_cycle_undirected,
    is_bipartite,
    kahn_topological_sort,
    kosaraju_scc,
    kruskal_mst,
    matrix_to_adj_list,
    prim_mst,
    shortest_path_unweighted,
)


def test_bfs_traversal_happy_path() -> None:
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert bfs_traversal(graph, 0) == [0, 1, 2, 3]


def test_shortest_path_unweighted_happy_path() -> None:
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert shortest_path_unweighted(graph, 0, 3) in ([0, 1, 3], [0, 2, 3])


def test_dfs_and_components_happy_path() -> None:
    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert dfs_traversal({0: [1], 1: []}, 0) == [0, 1]
    assert len(connected_components(graph)) == 2


def test_cycle_detection_variants_happy_path() -> None:
    assert has_cycle_undirected({0: [1], 1: [0, 2], 2: [1, 0]}) is True
    assert has_cycle_directed({0: [1], 1: [2], 2: [0]}) is True


def test_dijkstra_shortest_paths_happy_path() -> None:
    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    distances = dijkstra_shortest_paths(graph, 0)
    assert distances[3] == 4


def test_bellman_ford_happy_path() -> None:
    edges = [(0, 1, 5), (1, 2, 3), (0, 2, 10)]
    distances, has_negative_cycle = bellman_ford(3, edges, 0)
    assert distances[2] == 8
    assert has_negative_cycle is False


def test_floyd_warshall_happy_path() -> None:
    inf = 10**9
    matrix = [[0, 3, 1], [2, 0, inf], [1, 7, 0]]
    result = floyd_warshall(matrix)
    assert result[1][2] == 3


def test_mst_algorithms_happy_path() -> None:
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    assert kruskal_mst(4, edges) == 19

    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)],
    }
    assert prim_mst(graph, 0) == 16


def test_topological_sorts_happy_path() -> None:
    graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 1: [], 0: []}
    assert set(kahn_topological_sort(dict(graph))) == set(graph.keys())
    assert set(dfs_topological_sort(graph)) == set(graph.keys())


def test_dsu_union_find_happy_path() -> None:
    dsu = DSU(5)
    assert dsu.union(0, 1) is True
    assert dsu.union(1, 2) is True
    assert dsu.find(0) == dsu.find(2)
    assert dsu.union(0, 2) is False


def test_graph_representation_round_trip_happy_path() -> None:
    adjacency = edge_list_to_adj([(0, 1), (1, 2)], directed=False)
    matrix = adj_list_to_matrix(adjacency)
    recovered = matrix_to_adj_list(matrix)
    assert recovered[0] == [1]


def test_bipartite_and_scc_happy_path() -> None:
    assert is_bipartite({0: [1], 1: [0, 2], 2: [1]}) is True
    graph = {0: [1], 1: [2], 2: [0, 3], 3: []}
    components = [sorted(component) for component in kosaraju_scc(graph)]
    assert [0, 1, 2] in components

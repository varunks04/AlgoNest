from algonest.graphs import floyd_warshall


def test_floyd_warshall() -> None:
    inf = 10**9
    matrix = [[0, 3, 1], [2, 0, inf], [1, 7, 0]]
    result = floyd_warshall(matrix)
    assert result[1][2] == 3

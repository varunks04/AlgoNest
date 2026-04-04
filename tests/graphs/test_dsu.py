from algonest.graphs import DSU


def test_dsu() -> None:
    dsu = DSU(5)
    assert dsu.union(0, 1) is True
    assert dsu.union(1, 2) is True
    assert dsu.find(0) == dsu.find(2)
    assert dsu.union(0, 2) is False

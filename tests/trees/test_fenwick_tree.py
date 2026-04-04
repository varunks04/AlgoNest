from algonest.trees import FenwickTree


def test_fenwick_tree_ops() -> None:
    tree = FenwickTree(5)
    for idx, value in enumerate([1, 2, 3, 4, 5]):
        tree.point_update(idx, value)
    assert tree.prefix_sum(2) == 6
    assert tree.range_query(1, 3) == 9

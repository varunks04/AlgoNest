from algonest.trees import BST


def test_bst_ops() -> None:
    tree = BST()
    for value in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(value)
    assert tree.search(4) is True
    assert tree.floor(5) == 5
    assert tree.ceil(5) == 5
    assert tree.kth_smallest(3) == 4
    tree.delete(7)
    assert tree.search(7) is False

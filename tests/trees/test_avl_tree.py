from algonest.trees import AVLTree


def test_avl_tree_search() -> None:
    tree = AVLTree()
    for value in [10, 20, 30, 40, 50, 25]:
        tree.insert(value)
    assert tree.search(25) is True
    assert tree.search(99) is False

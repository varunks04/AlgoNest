from algonest.trees import BinaryTree


def test_binary_tree_core_ops() -> None:
    tree = BinaryTree()
    for value in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(value)
    assert tree.height() == 2
    assert tree.is_balanced() is True
    assert tree.lca(2, 4) == 3

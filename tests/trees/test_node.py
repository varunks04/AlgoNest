from algonest.trees import TreeNode


def test_tree_node_default_children() -> None:
    node = TreeNode(10)
    assert node.value == 10
    assert node.left is None
    assert node.right is None

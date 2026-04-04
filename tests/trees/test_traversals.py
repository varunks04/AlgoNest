from algonest.trees import TreeNode, inorder, level_order, postorder, preorder


def test_traversals() -> None:
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert inorder(root) == [2, 1, 3]
    assert inorder(root, iterative=True) == [2, 1, 3]
    assert preorder(root) == [1, 2, 3]
    assert postorder(root) == [2, 3, 1]
    assert level_order(root) == [1, 2, 3]

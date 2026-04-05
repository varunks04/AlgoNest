"""Tests for Phase 6 tree utilities."""

from algonest.trees import (
    TreeNode,
    build_from_preorder_inorder,
    count_nodes,
    deserialize,
    has_path_sum,
    is_balanced,
    lca_binary_tree,
    left_view,
    serialize,
    top_view,
)


def test_tree_construction_and_serialize_roundtrip() -> None:
    root = build_from_preorder_inorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    data = serialize(root)
    cloned = deserialize(data)
    assert serialize(cloned) == data


def test_tree_properties_and_views() -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert is_balanced(root) is True
    assert count_nodes(root) == 5
    assert has_path_sum(root, 7) is True
    assert left_view(root) == [1, 2, 4]
    assert top_view(root) == [4, 2, 1, 3]


def test_lca_binary_tree() -> None:
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    assert lca_binary_tree(root, 6, 2).value == 5

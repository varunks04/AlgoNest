"""Lowest common ancestor helpers."""

from typing import Optional

from algonest.trees.node import TreeNode


def lca_binary_tree(
    root: Optional[TreeNode], p_value: int, q_value: int
) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.value in (p_value, q_value):
        return root

    left = lca_binary_tree(root.left, p_value, q_value)
    right = lca_binary_tree(root.right, p_value, q_value)

    if left is not None and right is not None:
        return root
    return left if left is not None else right


def lca_bst(root: Optional[TreeNode], p_value: int, q_value: int) -> Optional[TreeNode]:
    node = root
    low = min(p_value, q_value)
    high = max(p_value, q_value)

    while node is not None:
        if node.value > high:
            node = node.left
        elif node.value < low:
            node = node.right
        else:
            return node

    return None

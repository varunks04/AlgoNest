"""Binary tree property helpers."""

from typing import Optional

from algonest.trees.node import TreeNode


def height(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def diameter(root: Optional[TreeNode]) -> int:
    best = 0

    def _dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left = _dfs(node.left)
        right = _dfs(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    _dfs(root)
    return best


def is_balanced(root: Optional[TreeNode]) -> bool:
    def _check(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = _check(node.left)
        if left == -1:
            return -1
        right = _check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return _check(root) != -1


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def _mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.value == b.value and _mirror(a.left, b.right) and _mirror(a.right, b.left)

    if root is None:
        return True
    return _mirror(root.left, root.right)


def count_nodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaves(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

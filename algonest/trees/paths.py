"""Path-related binary tree helpers."""

from typing import List, Optional

from algonest.trees.node import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.value == target_sum
    remain = target_sum - root.value
    return has_path_sum(root.left, remain) or has_path_sum(root.right, remain)


def root_to_leaf_paths(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    output: List[List[int]] = []

    def _dfs(node: TreeNode, path: List[int]) -> None:
        path.append(node.value)
        if node.left is None and node.right is None:
            output.append(path[:])
        else:
            if node.left is not None:
                _dfs(node.left, path)
            if node.right is not None:
                _dfs(node.right, path)
        path.pop()

    _dfs(root, [])
    return output


def max_path_sum(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    best = float("-inf")

    def _dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left = max(_dfs(node.left), 0)
        right = max(_dfs(node.right), 0)
        best = max(best, node.value + left + right)
        return node.value + max(left, right)

    _dfs(root)
    return int(best)

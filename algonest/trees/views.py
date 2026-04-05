"""Binary tree view helpers."""

from collections import deque
from typing import Deque, Dict, List, Optional, Tuple

from algonest.trees.node import TreeNode


def left_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    queue: Deque[TreeNode] = deque([root])
    output: List[int] = []

    while queue:
        level_size = len(queue)
        for level_index in range(level_size):
            node = queue.popleft()
            if level_index == 0:
                output.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return output


def right_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    queue: Deque[TreeNode] = deque([root])
    output: List[int] = []

    while queue:
        level_size = len(queue)
        for level_index in range(level_size):
            node = queue.popleft()
            if level_index == level_size - 1:
                output.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return output


def top_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    queue: Deque[Tuple[TreeNode, int]] = deque([(root, 0)])
    first_at_hd: Dict[int, int] = {}

    while queue:
        node, hd = queue.popleft()
        if hd not in first_at_hd:
            first_at_hd[hd] = node.value

        if node.left is not None:
            queue.append((node.left, hd - 1))
        if node.right is not None:
            queue.append((node.right, hd + 1))

    return [first_at_hd[k] for k in sorted(first_at_hd)]

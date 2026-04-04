"""Tree traversal algorithms (recursive and iterative)."""

from collections import deque
from typing import Deque, List, Optional

from algonest.trees.node import TreeNode


def inorder(root: Optional[TreeNode], iterative: bool = False) -> List[int]:
    """Return inorder traversal values.

    Args:
        root (Optional[TreeNode]): Root node.
        iterative (bool): Use iterative implementation when True.

    Returns:
        List[int]: Inorder values.
    """
    if not iterative:
        out: List[int] = []

        def _walk(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            _walk(node.left)
            out.append(node.value)
            _walk(node.right)

        _walk(root)
        return out

    out: List[int] = []
    stack: List[TreeNode] = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.value)
        node = node.right
    return out


def preorder(root: Optional[TreeNode], iterative: bool = False) -> List[int]:
    """Return preorder traversal values."""
    if root is None:
        return []
    if not iterative:
        out = [root.value]
        out.extend(preorder(root.left, iterative=False))
        out.extend(preorder(root.right, iterative=False))
        return out

    out: List[int] = []
    stack: List[TreeNode] = [root]
    while stack:
        node = stack.pop()
        out.append(node.value)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return out


def postorder(root: Optional[TreeNode], iterative: bool = False) -> List[int]:
    """Return postorder traversal values."""
    if not iterative:
        if root is None:
            return []
        out = postorder(root.left, iterative=False)
        out.extend(postorder(root.right, iterative=False))
        out.append(root.value)
        return out

    if root is None:
        return []
    out: List[int] = []
    stack: List[TreeNode] = [root]
    while stack:
        node = stack.pop()
        out.append(node.value)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return out[::-1]


def level_order(root: Optional[TreeNode]) -> List[int]:
    """Return level-order traversal values."""
    if root is None:
        return []
    out: List[int] = []
    queue: Deque[TreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        out.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return out

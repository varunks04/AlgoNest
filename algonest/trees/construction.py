"""Tree construction and serialization helpers."""

from collections import deque
from typing import Deque, List, Optional

from algonest.trees.node import TreeNode


def build_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) != len(inorder):
        raise ValueError("preorder and inorder must have same length")
    if not preorder:
        return None

    positions = {value: idx for idx, value in enumerate(inorder)}
    pre_idx = 0

    def _build(left: int, right: int) -> Optional[TreeNode]:
        nonlocal pre_idx
        if left > right:
            return None

        root_value = preorder[pre_idx]
        pre_idx += 1
        split = positions[root_value]

        root = TreeNode(root_value)
        root.left = _build(left, split - 1)
        root.right = _build(split + 1, right)
        return root

    return _build(0, len(inorder) - 1)


def serialize(root: Optional[TreeNode]) -> str:
    if root is None:
        return ""

    output: List[str] = []
    queue: Deque[Optional[TreeNode]] = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            output.append("#")
            continue
        output.append(str(node.value))
        queue.append(node.left)
        queue.append(node.right)

    while output and output[-1] == "#":
        output.pop()

    return ",".join(output)


def deserialize(data: str) -> Optional[TreeNode]:
    if not data:
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue: Deque[TreeNode] = deque([root])
    idx = 1

    while queue and idx < len(values):
        node = queue.popleft()

        if idx < len(values) and values[idx] != "#":
            node.left = TreeNode(int(values[idx]))
            queue.append(node.left)
        idx += 1

        if idx < len(values) and values[idx] != "#":
            node.right = TreeNode(int(values[idx]))
            queue.append(node.right)
        idx += 1

    return root

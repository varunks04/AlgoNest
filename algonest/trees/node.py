"""Node definitions for tree data structures."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    """Represent a binary tree node.

    Args:
        value (int): Node value.
        left (Optional[TreeNode]): Left child.
        right (Optional[TreeNode]): Right child.
    """

    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

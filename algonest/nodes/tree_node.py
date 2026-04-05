"""Canonical binary-tree node definition."""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class TreeNode:
    """Node for binary tree structures."""

    value: Any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

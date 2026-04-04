"""Binary tree utility operations."""

from typing import Optional

from algonest.trees.node import TreeNode


class BinaryTree:
    """Implement basic binary tree operations on integer values."""

    def __init__(self) -> None:
        """Initialize an empty binary tree."""
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        """Insert value in BST-style position.

        Args:
            value (int): Value to insert.

        Returns:
            None

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        if self.root is None:
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def height(self) -> int:
        """Return tree height measured in edges.

        Returns:
            int: Height, or -1 when tree is empty.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _height(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def is_balanced(self) -> bool:
        """Return whether tree is height-balanced.

        Returns:
            bool: True when balanced.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _check(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_h = _check(node.left)
            if left_h == -1:
                return -1
            right_h = _check(node.right)
            if right_h == -1:
                return -1
            if abs(left_h - right_h) > 1:
                return -1
            return 1 + max(left_h, right_h)

        return _check(self.root) != -1

    def lca(self, first: int, second: int) -> Optional[int]:
        """Return lowest common ancestor value in BST-shaped tree.

        Args:
            first (int): First value.
            second (int): Second value.

        Returns:
            Optional[int]: LCA value or None when tree is empty.

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        node = self.root
        low = min(first, second)
        high = max(first, second)

        while node is not None:
            if high < node.value:
                node = node.left
            elif low > node.value:
                node = node.right
            else:
                return node.value

        return None

"""Binary search tree implementation."""

from typing import List, Optional

from algonest.trees.node import TreeNode


class BST:
    """Implement a binary search tree with common query operations."""

    def __init__(self) -> None:
        """Initialize empty BST."""
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        """Insert value into BST.

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

        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                node = node.right

    def search(self, value: int) -> bool:
        """Return whether value exists in BST.

        Args:
            value (int): Value to find.

        Returns:
            bool: True when found.

        Time Complexity: O(h)
        Space Complexity: O(1)
        """
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def delete(self, value: int) -> None:
        """Delete one matching value from BST.

        Args:
            value (int): Value to delete.

        Returns:
            None

        Time Complexity: O(h)
        Space Complexity: O(h)
        """
        def _min(node: TreeNode) -> TreeNode:
            while node.left is not None:
                node = node.left
            return node

        def _delete(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
            if node is None:
                return None
            if target < node.value:
                node.left = _delete(node.left, target)
            elif target > node.value:
                node.right = _delete(node.right, target)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = _min(node.right)
                node.value = successor.value
                node.right = _delete(node.right, successor.value)
            return node

        self.root = _delete(self.root, value)

    def floor(self, value: int) -> Optional[int]:
        """Return greatest value less than or equal to given value."""
        node = self.root
        result: Optional[int] = None
        while node is not None:
            if node.value == value:
                return value
            if node.value < value:
                result = node.value
                node = node.right
            else:
                node = node.left
        return result

    def ceil(self, value: int) -> Optional[int]:
        """Return smallest value greater than or equal to given value."""
        node = self.root
        result: Optional[int] = None
        while node is not None:
            if node.value == value:
                return value
            if node.value > value:
                result = node.value
                node = node.left
            else:
                node = node.right
        return result

    def kth_smallest(self, k: int) -> Optional[int]:
        """Return kth smallest element (1-indexed).

        Args:
            k (int): Rank to fetch.

        Returns:
            Optional[int]: Value or None if k is invalid.
        """
        if k <= 0:
            return None
        stack: List[TreeNode] = []
        node = self.root
        count = 0
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.value
            node = node.right
        return None

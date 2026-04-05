"""AVL tree implementation with self-balancing insert."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AVLNode:
    """Represent a node in AVL tree."""

    value: int
    left: Optional["AVLNode"] = None
    right: Optional["AVLNode"] = None
    height: int = 1


class AVLTree:
    """Implement AVL tree with rotation-based balancing."""

    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def insert(self, value: int) -> None:
        """Insert value while maintaining AVL balance."""
        self.root = self._insert(self.root, value)

    def search(self, value: int) -> bool:
        """Return whether value exists in AVL tree."""
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node is not None else 0

    def _balance(self, node: Optional[AVLNode]) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        pivot_node = y.left
        assert pivot_node is not None
        transfer_subtree = pivot_node.right
        pivot_node.right = y
        y.left = transfer_subtree
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        pivot_node.height = 1 + max(
            self._height(pivot_node.left), self._height(pivot_node.right)
        )
        return pivot_node

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        pivot_node = x.right
        assert pivot_node is not None
        transfer_subtree = pivot_node.left
        pivot_node.left = x
        x.right = transfer_subtree
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        pivot_node.height = 1 + max(
            self._height(pivot_node.left), self._height(pivot_node.right)
        )
        return pivot_node

    def _insert(self, node: Optional[AVLNode], value: int) -> AVLNode:
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance(node)

        if balance > 1 and node.left is not None and value < node.left.value:
            return self._rotate_right(node)
        if balance < -1 and node.right is not None and value > node.right.value:
            return self._rotate_left(node)
        if balance > 1 and node.left is not None and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and node.right is not None and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

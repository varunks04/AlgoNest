"""Doubly linked list implementation."""

from typing import Any, List, Optional

from algonest.linked_list.node import DoublyListNode


class DoublyLinkedList:
    """Implement a doubly linked list with forward and backward traversal."""

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None

    def insert(self, value: Any) -> None:
        """Insert a value at the end of the list.

        Args:
            value (Any): Value to append.

        Returns:
            None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = DoublyListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        assert self.tail is not None
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete(self, value: Any) -> bool:
        """Delete the first node matching value.

        Args:
            value (Any): Value to remove.

        Returns:
            bool: True when removed, otherwise False.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next

        return False

    def to_list(self) -> List[Any]:
        """Return forward traversal values as a list.

        Returns:
            List[Any]: Values from head to tail.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        output: List[Any] = []
        current = self.head
        while current is not None:
            output.append(current.value)
            current = current.next
        return output

    def traverse_backward(self) -> List[Any]:
        """Return backward traversal values as a list.

        Returns:
            List[Any]: Values from tail to head.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        output: List[Any] = []
        current = self.tail
        while current is not None:
            output.append(current.value)
            current = current.prev
        return output

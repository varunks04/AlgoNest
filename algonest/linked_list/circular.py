"""Circular linked list implementation."""

from typing import Any, List, Optional

from algonest.linked_list.node import ListNode


class CircularLinkedList:
    """Implement a circular linked list with rotation and Josephus logic."""

    def __init__(self) -> None:
        """Initialize an empty circular linked list."""
        self.head: Optional[ListNode] = None

    def insert(self, value: Any) -> None:
        """Insert value at the end of circular list.

        Args:
            value (Any): Value to append.

        Returns:
            None

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        tail = self.head
        while tail.next is not self.head:
            assert tail.next is not None
            tail = tail.next
        tail.next = new_node
        new_node.next = self.head

    def rotate(self, k: int) -> None:
        """Rotate head pointer by k steps.

        Args:
            k (int): Number of forward steps.

        Returns:
            None

        Raises:
            TypeError: If k is not an integer.

        Time Complexity: O(k)
        Space Complexity: O(1)
        """
        if not isinstance(k, int) or isinstance(k, bool):
            raise TypeError("k must be an integer")
        if self.head is None:
            return

        steps = k % max(1, len(self.to_list()))
        for _ in range(steps):
            assert self.head is not None and self.head.next is not None
            self.head = self.head.next

    def josephus(self, step: int) -> Any:
        """Return survivor value using Josephus elimination process.

        Args:
            step (int): Every step-th node is removed.

        Returns:
            Any: Surviving node value.

        Raises:
            ValueError: If list is empty or step is not positive.

        Time Complexity: O(n * step)
        Space Complexity: O(1)
        """
        if self.head is None:
            raise ValueError("circular list is empty")
        if not isinstance(step, int) or isinstance(step, bool) or step <= 0:
            raise ValueError("step must be a positive integer")

        current = self.head
        previous = self.head
        while previous.next is not self.head:
            assert previous.next is not None
            previous = previous.next

        while current is not None and current.next is not current:
            for _ in range(step - 1):
                previous = current
                assert current.next is not None
                current = current.next
            previous.next = current.next
            current = current.next

        self.head = current
        assert current is not None
        return current.value

    def to_list(self) -> List[Any]:
        """Return values from one full circular traversal.

        Returns:
            List[Any]: Values from head back to head.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self.head is None:
            return []

        output = [self.head.value]
        current = self.head.next
        while current is not None and current is not self.head:
            output.append(current.value)
            current = current.next
        return output

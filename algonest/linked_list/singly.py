"""Singly linked list implementation."""

from typing import Any, List, Optional

from algonest.linked_list.node import ListNode


class SinglyLinkedList:
    """Implement a singly linked list with common operations."""

    def __init__(self) -> None:
        """Initialize an empty singly linked list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head: Optional[ListNode] = None

    def insert(self, value: Any) -> None:
        """Insert a value at the end of the list.

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
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, value: Any) -> bool:
        """Delete the first node matching value.

        Args:
            value (Any): Value to remove.

        Returns:
            bool: True when a node is removed, else False.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def reverse(self) -> None:
        """Reverse the list in place.

        Returns:
            None

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        previous: Optional[ListNode] = None
        current = self.head
        while current is not None:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def detect_cycle(self) -> bool:
        """Return True when the list contains a cycle.

        Returns:
            bool: Whether a cycle exists.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self) -> List[Any]:
        """Return list representation of linked list values.

        Returns:
            List[Any]: Values in list order.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        output: List[Any] = []
        current = self.head
        while current is not None:
            output.append(current.value)
            current = current.next
        return output

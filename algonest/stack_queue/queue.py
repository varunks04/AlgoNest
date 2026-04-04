"""Queue data structure implementation."""

from collections import deque
from typing import Any, Deque


class Queue:
    """Implement a FIFO queue."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._items: Deque[Any] = deque()

    def enqueue(self, value: Any) -> None:
        """Insert value at the back of queue.

        Args:
            value (Any): Value to add.

        Returns:
            None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items.append(value)

    def dequeue(self) -> Any:
        """Remove and return front value.

        Returns:
            Any: Front value.

        Raises:
            ValueError: If queue is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise ValueError("queue is empty")
        return self._items.popleft()

    def front(self) -> Any:
        """Return front value without removing it.

        Returns:
            Any: Front value.

        Raises:
            ValueError: If queue is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise ValueError("queue is empty")
        return self._items[0]

    def is_empty(self) -> bool:
        """Return whether queue has no elements.

        Returns:
            bool: True when empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items) == 0

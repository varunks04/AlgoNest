"""Deque data structure implementation."""

from collections import deque as std_deque
from typing import Any, Deque


class DequeDS:
    """Implement a double-ended queue wrapper."""

    def __init__(self) -> None:
        """Initialize an empty deque."""
        self._items: Deque[Any] = std_deque()

    def push_front(self, value: Any) -> None:
        """Push value at front.

        Args:
            value (Any): Value to add.

        Returns:
            None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items.appendleft(value)

    def push_back(self, value: Any) -> None:
        """Push value at back.

        Args:
            value (Any): Value to add.

        Returns:
            None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items.append(value)

    def pop_front(self) -> Any:
        """Pop and return front value.

        Returns:
            Any: Front value.

        Raises:
            ValueError: If deque is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise ValueError("deque is empty")
        return self._items.popleft()

    def pop_back(self) -> Any:
        """Pop and return back value.

        Returns:
            Any: Back value.

        Raises:
            ValueError: If deque is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise ValueError("deque is empty")
        return self._items.pop()

    def is_empty(self) -> bool:
        """Return whether deque is empty.

        Returns:
            bool: True when empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items) == 0

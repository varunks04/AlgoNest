"""Stack data structure implementation."""

from typing import Any, List


class Stack:
    """Implement a LIFO stack."""

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: List[Any] = []

    def push(self, value: Any) -> None:
        """Push a value onto stack.

        Args:
            value (Any): Value to push.

        Returns:
            None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items.append(value)

    def pop(self) -> Any:
        """Pop and return top value.

        Returns:
            Any: Last pushed value.

        Raises:
            ValueError: If stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise ValueError("stack is empty")
        return self._items.pop()

    def peek(self) -> Any:
        """Return top value without removing it.

        Returns:
            Any: Current top value.

        Raises:
            ValueError: If stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise ValueError("stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return whether stack has no elements.

        Returns:
            bool: True when empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items) == 0

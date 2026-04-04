"""Priority queue implementation with custom key support."""

from typing import Any, Callable, List, Optional


class PriorityQueue:
    """Implement a priority queue using a binary heap and custom comparator."""

    def __init__(
        self,
        key: Optional[Callable[[Any], Any]] = None,
        min_priority: bool = True,
    ) -> None:
        """Initialize priority queue.

        Args:
            key (Optional[Callable[[Any], Any]]): Key extractor for comparisons.
            min_priority (bool): True for min-priority, False for max-priority.

        Returns:
            None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._data: List[Any] = []
        self._key = key if key is not None else (lambda x: x)
        self._min_priority = min_priority

    def push(self, value: Any) -> None:
        """Insert value into priority queue.

        Args:
            value (Any): Value to insert.

        Returns:
            None

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> Any:
        """Remove and return highest-priority value.

        Returns:
            Any: Highest-priority value.

        Raises:
            ValueError: If priority queue is empty.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not self._data:
            raise ValueError("priority queue is empty")

        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def peek(self) -> Any:
        """Return highest-priority value without removal.

        Returns:
            Any: Highest-priority value.

        Raises:
            ValueError: If priority queue is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._data:
            raise ValueError("priority queue is empty")
        return self._data[0]

    def is_empty(self) -> bool:
        """Return whether priority queue is empty.

        Returns:
            bool: True when empty.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._data) == 0

    def _higher_priority(self, left: Any, right: Any) -> bool:
        left_key = self._key(left)
        right_key = self._key(right)
        if self._min_priority:
            return left_key < right_key
        return left_key > right_key

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if not self._higher_priority(self._data[index], self._data[parent]):
                break
            self._data[parent], self._data[index] = self._data[index], self._data[parent]
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self._data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            candidate = index

            if left < size and self._higher_priority(self._data[left], self._data[candidate]):
                candidate = left
            if right < size and self._higher_priority(self._data[right], self._data[candidate]):
                candidate = right

            if candidate == index:
                break

            self._data[index], self._data[candidate] = (
                self._data[candidate],
                self._data[index],
            )
            index = candidate

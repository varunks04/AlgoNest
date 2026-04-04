"""Min-heap data structure implementation."""

from typing import Any, List


class MinHeap:
    """Implement a binary min-heap."""

    def __init__(self) -> None:
        """Initialize an empty min-heap."""
        self.data: List[Any] = []

    def insert(self, value: Any) -> None:
        """Insert value into the heap.

        Args:
            value (Any): Value to insert.

        Returns:
            None

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def extract_min(self) -> Any:
        """Remove and return minimum value.

        Returns:
            Any: Minimum heap value.

        Raises:
            ValueError: If heap is empty.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if not self.data:
            raise ValueError("heap is empty")

        minimum = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return minimum

    def heapify(self, values: List[Any]) -> None:
        """Build min-heap from input list.

        Args:
            values (List[Any]): Input list.

        Returns:
            None

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not isinstance(values, list):
            raise TypeError("values must be a list")
        self.data = values[:]
        for index in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(index)

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self.data[parent] <= self.data[index]:
                break
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            index = smallest

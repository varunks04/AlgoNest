"""Fixed-capacity circular queue implementation."""

from typing import Any, List


class CircularQueue:
    """Ring-buffer queue with O(1) enqueue/dequeue."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._data: List[Any] = [None] * capacity
        self._front = 0
        self._size = 0

    def enqueue(self, value: Any) -> bool:
        if self.is_full():
            return False
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = value
        self._size += 1
        return True

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("queue is empty")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("queue is empty")
        return self._data[self._front]

    def rear(self) -> Any:
        if self.is_empty():
            raise IndexError("queue is empty")
        idx = (self._front + self._size - 1) % self._capacity
        return self._data[idx]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

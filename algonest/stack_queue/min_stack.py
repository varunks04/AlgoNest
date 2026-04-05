"""Minimum-stack data structure."""

from typing import List


class MinStack:
    """Stack with O(1) retrieval of current minimum."""

    def __init__(self) -> None:
        self._values: List[int] = []
        self._mins: List[int] = []

    def push(self, value: int) -> None:
        self._values.append(value)
        if not self._mins or value <= self._mins[-1]:
            self._mins.append(value)

    def pop(self) -> int:
        if not self._values:
            raise IndexError("stack is empty")
        value = self._values.pop()
        if value == self._mins[-1]:
            self._mins.pop()
        return value

    def top(self) -> int:
        if not self._values:
            raise IndexError("stack is empty")
        return self._values[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("stack is empty")
        return self._mins[-1]

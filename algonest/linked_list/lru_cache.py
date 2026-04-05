"""LRU cache implementation using hashmap + doubly-linked list."""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class _Node:
    key: int
    value: int
    prev: Optional["_Node"] = None
    next: Optional["_Node"] = None


class LRUCache:
    """Fixed-capacity least-recently-used cache."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.lookup: Dict[int, _Node] = {}
        self.head = _Node(0, 0)
        self.tail = _Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.lookup.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.lookup.get(key)
        if node is not None:
            node.value = value
            self._move_to_front(node)
            return

        if len(self.lookup) >= self.capacity:
            lru = self.tail.prev
            if lru is not None and lru is not self.head:
                self._detach(lru)
                del self.lookup[lru.key]

        new_node = _Node(key, value)
        self.lookup[key] = new_node
        self._attach_after_head(new_node)

    def _detach(self, node: _Node) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node

    def _attach_after_head(self, node: _Node) -> None:
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        if first is not None:
            first.prev = node

    def _move_to_front(self, node: _Node) -> None:
        self._detach(node)
        self._attach_after_head(node)

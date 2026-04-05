"""Node definitions for linked list data structures."""

from dataclasses import dataclass
from typing import Any, Optional
from algonest.nodes import ListNode


@dataclass
class DoublyListNode:
    """Represent a node in a doubly linked list.

    Attributes:
        value (Any): Node payload value.
        prev (Optional[DoublyListNode]): Pointer to previous node.
        next (Optional[DoublyListNode]): Pointer to next node.
    """

    value: Any
    prev: Optional["DoublyListNode"] = None
    next: Optional["DoublyListNode"] = None

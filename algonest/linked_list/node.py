"""Node definitions for linked list data structures."""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ListNode:
    """Represent a node in a singly linked list.

    Attributes:
        value (Any): Node payload value.
        next (Optional[ListNode]): Pointer to next node.
    """

    value: Any
    next: Optional["ListNode"] = None


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

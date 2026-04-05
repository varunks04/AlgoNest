"""Cycle detection utilities for linked lists."""

from typing import Optional

from algonest.linked_list.node import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    """Return whether linked list contains a cycle."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def find_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return cycle entry node or None when acyclic."""
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow


def cycle_length(head: Optional[ListNode]) -> int:
    """Return cycle length, or 0 for acyclic list."""
    start = find_cycle_start(head)
    if start is None:
        return 0

    count = 1
    current = start.next
    while current is not start:
        current = current.next
        count += 1
    return count

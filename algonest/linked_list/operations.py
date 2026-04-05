"""Reusable linked-list utility operations."""

from typing import Optional

from algonest.linked_list.node import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return head of reversed list."""
    prev: Optional[ListNode] = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def reverse_in_groups(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverse list in groups of size k and return new head."""
    if k <= 1 or head is None:
        return head

    count = 0
    current = head
    while current is not None and count < k:
        current = current.next
        count += 1
    if count < k:
        return head

    prev: Optional[ListNode] = None
    current = head
    count = 0
    while current is not None and count < k:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        count += 1

    head.next = reverse_in_groups(current, k)
    return prev


def merge_two_sorted(
    left: Optional[ListNode], right: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted lists and return merged head."""
    dummy = ListNode(0)
    tail = dummy

    while left is not None and right is not None:
        if left.value <= right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left is not None else right
    return dummy.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the nth node from end and return head."""
    if n <= 0:
        raise ValueError("n must be positive")

    dummy = ListNode(0, head)
    fast: Optional[ListNode] = dummy
    slow: Optional[ListNode] = dummy

    for _ in range(n):
        if fast is None or fast.next is None:
            raise IndexError("n is larger than list length")
        fast = fast.next

    while fast is not None and fast.next is not None:
        fast = fast.next
        slow = slow.next

    if slow is not None and slow.next is not None:
        slow.next = slow.next.next

    return dummy.next


def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return middle node (second middle for even length)."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

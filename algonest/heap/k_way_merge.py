"""Heap-based k-way merge helpers."""

import heapq
from typing import List, Optional, Sequence, Tuple

from algonest.linked_list.node import ListNode


def merge_k_sorted_arrays(arrays: Sequence[Sequence[int]]) -> List[int]:
    """Merge sorted arrays into one sorted array."""
    heap: List[Tuple[int, int, int]] = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    output: List[int] = []
    while heap:
        value, arr_idx, idx = heapq.heappop(heap)
        output.append(value)
        next_idx = idx + 1
        if next_idx < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][next_idx], arr_idx, next_idx))

    return output


def merge_k_sorted_lists(lists: Sequence[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge sorted linked lists and return merged head."""
    heap: List[Tuple[int, int, ListNode]] = []
    counter = 0
    for node in lists:
        if node is not None:
            heapq.heappush(heap, (node.value, counter, node))
            counter += 1

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.value, counter, node.next))
            counter += 1

    tail.next = None
    return dummy.next

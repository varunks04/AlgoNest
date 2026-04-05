"""Tests for Phase 6 linked-list utilities."""

from algonest.linked_list import (
    LRUCache,
    ListNode,
    cycle_length,
    find_middle,
    has_cycle,
    merge_two_sorted,
    reverse_list,
)


def _build(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def _to_list(head):
    out = []
    current = head
    while current is not None:
        out.append(current.value)
        current = current.next
    return out


def test_reverse_list_and_merge_two_sorted() -> None:
    assert _to_list(reverse_list(_build([1, 2, 3]))) == [3, 2, 1]
    merged = merge_two_sorted(_build([1, 4]), _build([2, 3]))
    assert _to_list(merged) == [1, 2, 3, 4]


def test_find_middle_and_cycle_length() -> None:
    head = _build([1, 2, 3, 4])
    assert find_middle(head).value == 3

    cycle_head = _build([1, 2, 3])
    cycle_head.next.next.next = cycle_head.next
    assert has_cycle(cycle_head) is True
    assert cycle_length(cycle_head) == 2


def test_lru_cache_eviction() -> None:
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10
    cache.put(3, 30)
    assert cache.get(2) == -1

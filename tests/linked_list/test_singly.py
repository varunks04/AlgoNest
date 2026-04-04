"""Tests for SinglyLinkedList."""

from algonest.linked_list import SinglyLinkedList


def test_singly_insert_delete_reverse_and_to_list() -> None:
    linked = SinglyLinkedList()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)
    assert linked.to_list() == [1, 2, 3]

    assert linked.delete(2) is True
    assert linked.to_list() == [1, 3]

    linked.reverse()
    assert linked.to_list() == [3, 1]


def test_singly_detect_cycle_false_by_default() -> None:
    linked = SinglyLinkedList()
    linked.insert(1)
    linked.insert(2)
    assert linked.detect_cycle() is False


def test_singly_detect_cycle_true_when_manually_connected() -> None:
    linked = SinglyLinkedList()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)

    head = linked.head
    assert head is not None and head.next is not None and head.next.next is not None
    head.next.next.next = head
    assert linked.detect_cycle() is True

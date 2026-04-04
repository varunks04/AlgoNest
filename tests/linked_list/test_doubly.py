"""Tests for DoublyLinkedList."""

from algonest.linked_list import DoublyLinkedList


def test_doubly_insert_delete_and_traverse_backward() -> None:
    linked = DoublyLinkedList()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)

    assert linked.to_list() == [1, 2, 3]
    assert linked.traverse_backward() == [3, 2, 1]

    assert linked.delete(2) is True
    assert linked.to_list() == [1, 3]
    assert linked.traverse_backward() == [3, 1]

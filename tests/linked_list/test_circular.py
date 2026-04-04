"""Tests for CircularLinkedList."""

import pytest

from algonest.linked_list import CircularLinkedList


def test_circular_insert_rotate_and_to_list() -> None:
    linked = CircularLinkedList()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)

    assert linked.to_list() == [1, 2, 3]
    linked.rotate(1)
    assert linked.to_list() == [2, 3, 1]


def test_circular_josephus_returns_survivor() -> None:
    linked = CircularLinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked.insert(value)
    assert linked.josephus(2) == 3


def test_circular_josephus_raises_on_empty_list() -> None:
    linked = CircularLinkedList()
    with pytest.raises(ValueError, match="empty"):
        linked.josephus(2)

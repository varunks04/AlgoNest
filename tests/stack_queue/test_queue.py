"""Tests for Queue."""

import pytest

from algonest.stack_queue import Queue


def test_queue_enqueue_dequeue_front_and_empty() -> None:
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() is True


def test_queue_dequeue_raises_when_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        Queue().dequeue()

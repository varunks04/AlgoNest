"""Tests for PriorityQueue."""

import pytest

from algonest.heap import PriorityQueue


def test_priority_queue_min_mode() -> None:
    queue = PriorityQueue()
    queue.push(3)
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3


def test_priority_queue_max_mode_and_custom_key() -> None:
    queue = PriorityQueue(key=lambda item: item["p"], min_priority=False)
    queue.push({"p": 1, "task": "low"})
    queue.push({"p": 3, "task": "high"})
    queue.push({"p": 2, "task": "mid"})
    assert queue.pop()["task"] == "high"


def test_priority_queue_pop_raises_when_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        PriorityQueue().pop()

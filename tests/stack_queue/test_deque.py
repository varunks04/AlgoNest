"""Tests for DequeDS."""

import pytest

from algonest.stack_queue import DequeDS


def test_deque_push_pop_both_ends() -> None:
    deq = DequeDS()
    deq.push_back(2)
    deq.push_front(1)
    deq.push_back(3)
    assert deq.pop_front() == 1
    assert deq.pop_back() == 3
    assert deq.pop_back() == 2


def test_deque_pop_raises_when_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        DequeDS().pop_front()

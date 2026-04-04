"""Tests for Stack."""

import pytest

from algonest.stack_queue import Stack


def test_stack_push_pop_peek_and_empty() -> None:
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() is True


def test_stack_pop_raises_when_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        Stack().pop()

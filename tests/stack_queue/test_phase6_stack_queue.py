"""Tests for Phase 6 stack/queue utilities."""

from algonest.stack_queue import (
    CircularQueue,
    MinStack,
    evaluate_postfix,
    infix_to_postfix,
    valid_parentheses,
)


def test_min_stack() -> None:
    st = MinStack()
    st.push(3)
    st.push(1)
    st.push(2)
    assert st.get_min() == 1
    st.pop()
    st.pop()
    assert st.get_min() == 3


def test_circular_queue() -> None:
    q = CircularQueue(2)
    assert q.enqueue(1) is True
    assert q.enqueue(2) is True
    assert q.enqueue(3) is False
    assert q.dequeue() == 1
    assert q.enqueue(3) is True
    assert q.rear() == 3


def test_expression_helpers() -> None:
    assert valid_parentheses("([{}])") is True
    postfix = infix_to_postfix("3 + 4 * 2")
    assert postfix == "3 4 2 * +"
    assert evaluate_postfix(postfix) == 11.0

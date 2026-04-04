"""Stack and queue data structures package."""

from algonest.stack_queue.deque import DequeDS
from algonest.stack_queue.monotonic_stack import largest_rectangle_in_histogram, next_greater_element
from algonest.stack_queue.queue import Queue
from algonest.stack_queue.stack import Stack

__all__ = [
    "Stack",
    "Queue",
    "DequeDS",
    "next_greater_element",
    "largest_rectangle_in_histogram",
]

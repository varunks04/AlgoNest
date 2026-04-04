"""Tests for MaxHeap."""

import pytest

from algonest.heap import MaxHeap


def test_max_heap_insert_extract_and_heapify() -> None:
    heap = MaxHeap()
    heap.heapify([5, 3, 8, 1])
    assert heap.extract_max() == 8
    heap.insert(10)
    assert heap.extract_max() == 10


def test_max_heap_extract_raises_when_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        MaxHeap().extract_max()

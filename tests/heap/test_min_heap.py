"""Tests for MinHeap."""

import pytest

from algonest.heap import MinHeap


def test_min_heap_insert_extract_and_heapify() -> None:
    heap = MinHeap()
    heap.heapify([5, 3, 8, 1])
    assert heap.extract_min() == 1
    heap.insert(2)
    assert heap.extract_min() == 2


def test_min_heap_extract_raises_when_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        MinHeap().extract_min()

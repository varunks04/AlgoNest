# API Guide

This guide describes practical usage patterns for algonest APIs.

## Import Style

Prefer root imports for common workflows:

```python
from algonest import binary_search, merge_sort, Trie
```

## Input Contract

Array-like algorithm functions accept iterables and convert internally to lists.
For invalid input (`None` or non-iterable), validation raises:

```python
TypeError("Input must not be None")
```

## Data Structure Usage

Use object APIs for stateful structures:

```python
from algonest import MinHeap

heap = MinHeap()
heap.insert(3)
heap.insert(1)
print(heap.extract_min())
```

## Running Tests

From repository root:

```bash
python -m pytest -q tests
```

## Benchmarks

Run sample benchmark script:

```bash
python benchmarks/compare_algorithms.py
```

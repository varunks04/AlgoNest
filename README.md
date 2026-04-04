# AlgoNest

algonest is a clean, reusable Python DSA utility package focused on production-ready implementations of core algorithmic patterns.

## Installation

```bash
pip install algonest
```

## Included Modules

- `algonest.search.binary_search`: `lower_bound`, `upper_bound`, `binary_search`
- `algonest.arrays.sliding_window`: `max_sum_subarray_k`, `longest_unique_substring`
- `algonest.sort.sorting`: classical sorting algorithms
- `algonest.linked_list`: linked list data structures
- `algonest.stack_queue`: stack, queue, deque, monotonic stack utilities
- `algonest.heap`: min heap, max heap, priority queue
- `algonest.trees`: binary trees, BST/AVL, traversals, segment/fenwick trees
- `algonest.graphs`: traversal, shortest path, MST, DSU, topological sorting
- `algonest.dynamic_programming`: knapsack, LCS/LIS, coin change, MCM, edit distance
- `algonest.strings`: KMP, Rabin-Karp, Z algorithm, trie, anagram utilities
- `algonest.math`: gcd/lcm, prime utilities, modular arithmetic, bit tricks
- `algonest.utils`: validators and shared type helper aliases

## Quick Start

```python
from algonest import (
	binary_search,
	longest_unique_substring,
	lower_bound,
	max_sum_subarray_k,
	upper_bound,
)

idx = lower_bound([1, 2, 2, 4], 2)
hi = upper_bound([1, 2, 2, 4], 2)
pos = binary_search([1, 3, 5, 7], 5)
best = max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3)
size = longest_unique_substring("abcabcbb")
```

## Testing

```bash
python -m pytest -q tests
```

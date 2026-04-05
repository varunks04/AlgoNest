# AlgoNest

AlgoNest is a Python toolkit for reusable algorithms, data structures, and small utility helpers.
It gives developers a consistent, iterable-first API for common problems without rebuilding the same primitives each time.

## Problem Statement

Many algorithm libraries are either classroom examples or narrow problem-specific snippets. AlgoNest is built as a practical toolkit instead: a collection of reusable building blocks for search, sorting, trees, graphs, dynamic programming, strings, math, and supporting utilities. It is useful when you want clean, typed implementations that are easy to import, compose, and reuse in exercises, interview prep, and real code.

## Target Audience

AlgoNest is for:

- Students learning core data structures and algorithm patterns
- Developers preparing for interviews
- Engineers who want reliable reference implementations
- Maintainers who need compact reusable helpers instead of one-off snippets

## Key Features

- `arrays/`: interval helpers, prefix sums, two pointers, Kadane, rotations, and matrix utilities
- `search/`: linear, binary, rotated, exponential, interpolation, jump, ternary, and 2D matrix search
- `sort/`: classic and advanced sorting implementations
- `linked_list/`: singly, doubly, and circular list structures plus linked-list algorithms
- `stack_queue/`: stacks, queues, deques, monotonic stack utilities, and expression helpers
- `heap/`: min/max heaps, priority queue, top-k helpers, merge helpers, and median tracking
- `trees/`: binary trees, BSTs, AVL trees, segment trees, Fenwick trees, traversals, views, and path helpers
- `graphs/`: traversal, shortest path, MST, SCC, bipartite, DSU, and representation helpers
- `dynamic_programming/`: Fibonacci, knapsack, coin change, LCS, LIS, edit distance, subset DP, and grid DP
- `strings/`: trie, anagram helpers, KMP, Rabin-Karp, Z algorithm, rolling hash, and palindrome helpers
- `math/`: number theory, modular arithmetic, combinatorics, matrix math, statistics, and bit manipulation
- `backtracking/`: combinations, permutations, subsets, and combination sum helpers
- `greedy/`: activity selection, fractional knapsack, jump-game helpers, and reachability logic
- `nodes/` and `utils/`: shared node types, validation, testing helpers, I/O helpers, and debug utilities

## Installation

```bash
pip install algonest
```

For local development:

```bash
pip install -e .
```

## Quick Usage Examples

### Search

```python
from algonest import binary_search, search_2d_matrix

index = binary_search([1, 3, 5, 7, 9], 7)
location = search_2d_matrix([[1, 4, 7], [10, 13, 16]], 13)
```

### Arrays

```python
from algonest import max_subarray_sum, prefix_sum, range_sum

best = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
prefix_values = prefix_sum([1, 2, 3, 4])
window_total = range_sum(prefix_values, 1, 3)
```

### Trees

```python
from algonest import BinaryTree

tree = BinaryTree()
for value in [5, 3, 8, 1, 4]:
	tree.insert(value)

height = tree.height()
balanced = tree.is_balanced()
```

### Strings

```python
from algonest import Trie, kmp_search

trie = Trie()
trie.insert("algo")
matches = kmp_search("ababcabcab", "abc")
```

## Project Structure

```text
AlgoNest/
|-- algonest/
|   |-- arrays/
|   |-- backtracking/
|   |-- dynamic_programming/
|   |-- graphs/
|   |-- greedy/
|   |-- heap/
|   |-- linked_list/
|   |-- math/
|   |-- nodes/
|   |-- search/
|   |-- sort/
|   |-- stack_queue/
|   |-- strings/
|   |-- trees/
|   `-- utils/
|-- benchmarks/
|-- docs/
|   `-- Project Structure.md
|-- tests/
|-- ALGONEST_API.md
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- README.md
`-- pyproject.toml
```

## Design Philosophy

AlgoNest is a toolkit, not a problem bank. The goal is to provide small, reusable implementations with consistent naming, clear signatures, and predictable behavior so the package is useful as a reference and as a foundation for real code.

## Development Notes

- Tests are organized with `pytest` under `tests/`.
- Public API signatures are documented in `ALGONEST_API.md`.
- Contribution guidance is in `CONTRIBUTING.md`.

## License

AlgoNest is released under the MIT License. See `LICENSE` for details.

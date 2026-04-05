# Project Structure

AlgoNest follows a standard Python package layout. Public algorithms live under `algonest/`, with tests, benchmarks, and documentation at repository root.

```text
AlgoNest/
|-- algonest/
|   |-- arrays/              # Array patterns, interval helpers, matrix helpers
|   |-- backtracking/        # Combinations, permutations, subsets
|   |-- dynamic_programming/ # Fibonacci, knapsack, LCS/LIS, coin change, grid DP
|   |-- graphs/              # Traversal, shortest path, MST, DSU, representation helpers
|   |-- greedy/              # Activity selection, knapsack, jump-game helpers
|   |-- heap/                # Min/max heap, priority queue, k-element helpers
|   |-- linked_list/         # Linked-list structures and operations
|   |-- math/                # Number theory, combinatorics, matrix math, statistics
|   |-- nodes/               # Canonical node types shared across modules
|   |-- search/              # Linear, binary, rotated, jump, 2D matrix search
|   |-- sort/                # Core and advanced sorting implementations
|   |-- stack_queue/         # Stack, queue, deque, expression, monotonic stack
|   |-- strings/             # Trie, hashes, substring search, palindrome helpers
|   |-- trees/               # Binary trees, BSTs, AVL, Fenwick, segment trees
|   `-- utils/               # Validation, debug, I/O, and test helpers
|-- benchmarks/              # Performance comparison scripts
|-- docs/                    # Supplementary documentation
|-- tests/                   # Pytest suites mirroring the package modules
|-- ALGONEST_API.md          # Public API map
|-- README.md                # Project overview and usage guide
`-- pyproject.toml           # Packaging metadata and dependencies
```

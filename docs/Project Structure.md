# Project Structure

AlgoNest uses a conventional Python package layout.
Source code lives in `algonest/`, with tests, docs, and project configuration at repository root.

```text
AlgoNest/
|-- algonest/
|   |-- arrays/                 # Array and two-pointer patterns
|   |-- search/                 # Linear, binary, ternary, jump search
|   |-- sort/                   # Comparison and non-comparison sorting
|   |-- linked_list/            # Linked list nodes and list variants
|   |-- stack_queue/            # Stack, queue, deque, monotonic stack
|   |-- heap/                   # MinHeap, MaxHeap, PriorityQueue
|   |-- trees/                  # Tree structures and traversals
|   |-- graphs/                 # Graph traversal, shortest paths, MST, DSU
|   |-- dynamic_programming/    # Knapsack, LCS/LIS, coin change, matrix chain
|   |-- strings/                # KMP, Rabin-Karp, Z algorithm, trie, anagram
|   |-- math/                   # Number theory and bit manipulation
|   `-- utils/                  # Validation, debug, I/O, test runner helpers
|-- tests/                      # Pytest suites mirroring package modules
|-- benchmarks/                 # Performance comparison scripts
|-- docs/                       # Supplementary project documentation
|-- README.md                   # Project overview and quick start
|-- API_GUIDE.md                # API signatures and usage references
`-- pyproject.toml              # Packaging and dependency metadata
```

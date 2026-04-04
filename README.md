# AlgoNest

AlgoNest is a Python algorithms and data structures library with a unified, iterable-first API.
It is designed for interview prep, education, and production utility code where correctness and readability matter.
The package provides reusable implementations with consistent naming and behavior across modules.

## Key Features

- Unified API exposed from package root (`from algonest import ...`)
- Broad coverage: arrays, search, sort, trees, graphs, dynamic programming, strings, math, and utilities
- Iterable-first function contracts for flexible inputs
- Stable behavior with explicit validation and predictable error handling
- Lightweight package footprint with no required runtime dependencies

## Installation

```bash
pip install algonest
```

## Quick Usage Examples

### Search: `binary_search`

```python
from algonest import binary_search

index = binary_search([1, 3, 5, 7, 9], 7)
print(index)  # 3
```

### Arrays: `max_subarray_sum` (Kadane)

```python
from algonest import max_subarray_sum

best = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(best)  # 6
```

### Sort: `merge_sort`

```python
from algonest import merge_sort

sorted_values = merge_sort([5, 2, 9, 1])
print(sorted_values)  # [1, 2, 5, 9]
```

## Supported Data Types

AlgoNest APIs are built around iterable inputs and internal list conversion.

- `list`: fully supported
- `tuple`: fully supported
- NumPy arrays: supported when NumPy is installed, because arrays are iterable
- Custom nodes and data structures: provided for linked lists and trees (`ListNode`, `DoublyListNode`, `TreeNode`)

## Project Structure

```text
AlgoNest/
|-- algonest/
|   |-- arrays/
|   |-- search/
|   |-- sort/
|   |-- linked_list/
|   |-- stack_queue/
|   |-- heap/
|   |-- trees/
|   |-- graphs/
|   |-- dynamic_programming/
|   |-- strings/
|   |-- math/
|   `-- utils/
|-- tests/
|-- benchmarks/
|-- docs/
|-- API_GUIDE.md
`-- pyproject.toml
```

## Design Principles

- Consistency: common naming and predictable return behavior
- Reusability: modular algorithms and data structures that compose well
- Simplicity: clear function contracts and minimal API friction
- Performance: practical implementations with documented complexity

## Roadmap

- Phase 1: Core algorithms (search, sort, arrays)
- Phase 2: Core data structures (linked lists, stack/queue, heap)
- Phase 3: Advanced algorithms (trees, graphs, dynamic programming)
- Phase 4: Specialized modules (strings, math, utilities)
- Phase 5: Ecosystem quality (packaging, docs, tests, CI)

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for setup, test commands, and pull request guidelines.

## License

AlgoNest is released under the MIT License. See `LICENSE` for details.

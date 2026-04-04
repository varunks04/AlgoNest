# API Guide

This guide documents the primary public APIs exported from `algonest`.

## Import Patterns

Use root imports for common workflows:

```python
from algonest import binary_search, max_subarray_sum, merge_sort
from algonest import MinHeap, Trie
```

Use module imports when grouping related calls:

```python
from algonest import arrays, search, sort
```

## Input and Validation Contract

- Most algorithm functions accept `Iterable[...]` and convert inputs internally to `list`.
- Invalid inputs raise:
	- `TypeError("Input must not be None")`
	- `TypeError("Input must be iterable")`
- Some functions enforce additional constraints (for example, numeric-only arrays).

## Search Module

### `binary_search(arr: Iterable[T], target: T) -> int`

- Parameters:
	- `arr`: sorted iterable of comparable values
	- `target`: value to locate
- Returns: index of `target`, or `-1` if not found

```python
from algonest import binary_search

binary_search([1, 3, 5, 7], 5)  # 2
```

### `lower_bound(arr: Iterable[T], target: T) -> int`

- Parameters:
	- `arr`: sorted iterable
	- `target`: boundary value
- Returns: first index `i` where `arr[i] >= target`, or `len(arr)`

```python
from algonest import lower_bound

lower_bound([1, 2, 2, 4], 2)  # 1
```

### `upper_bound(arr: Iterable[T], target: T) -> int`

- Parameters:
	- `arr`: sorted iterable
	- `target`: boundary value
- Returns: first index `i` where `arr[i] > target`, or `len(arr)`

```python
from algonest import upper_bound

upper_bound([1, 2, 2, 4], 2)  # 3
```

## Arrays Module

### `max_subarray_sum(arr: Iterable[Real]) -> Real`

- Parameters:
	- `arr`: numeric iterable
- Returns: maximum contiguous subarray sum

```python
from algonest import max_subarray_sum

max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])  # 6
```

### `prefix_sum(arr: Iterable[Real]) -> List[Real]`

- Parameters:
	- `arr`: numeric iterable
- Returns: prefix-sum array

```python
from algonest import prefix_sum

prefix_sum([3, 5, 2, 7])  # [3, 8, 10, 17]
```

### `range_sum(prefix: Iterable[Real], left: int, right: int) -> Real`

- Parameters:
	- `prefix`: prefix-sum iterable
	- `left`: left index (inclusive)
	- `right`: right index (inclusive)
- Returns: sum of original range `[left, right]`

```python
from algonest import prefix_sum, range_sum

p = prefix_sum([3, 5, 2, 7])
range_sum(p, 1, 3)  # 14
```

## Sort Module

### `merge_sort(arr: Iterable[Any]) -> List[Any]`

- Parameters:
	- `arr`: iterable of comparable values
- Returns: new sorted list

```python
from algonest import merge_sort

merge_sort([3, 1, 2])  # [1, 2, 3]
```

### `quick_sort(arr: Iterable[Any]) -> List[Any]`

- Parameters:
	- `arr`: iterable of comparable values
- Returns: new sorted list

```python
from algonest import quick_sort

quick_sort([10, 4, 7, 1])  # [1, 4, 7, 10]
```

### `counting_sort(arr: Iterable[Any]) -> List[int]`

- Parameters:
	- `arr`: iterable of integers
- Returns: sorted integer list

```python
from algonest import counting_sort

counting_sort([4, 1, 3, 1])  # [1, 1, 3, 4]
```

## Graphs Module

### `dijkstra_shortest_paths(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, int]`

- Parameters:
	- `graph`: adjacency list of `(neighbor, weight)` pairs
	- `source`: source node
- Returns: shortest known distance from source to each node key in graph

```python
from algonest import dijkstra_shortest_paths

graph = {
		0: [(1, 4), (2, 1)],
		1: [(3, 1)],
		2: [(1, 2), (3, 5)],
		3: [],
}
dijkstra_shortest_paths(graph, 0)  # {0: 0, 1: 3, 2: 1, 3: 4}
```

## Dynamic Programming Module

### `lcs_length(first: str, second: str) -> int`

- Parameters:
	- `first`: first string
	- `second`: second string
- Returns: length of the longest common subsequence

```python
from algonest import lcs_length

lcs_length("abcde", "ace")  # 3
```

### `knapsack_01(weights: List[int], values: List[int], capacity: int) -> int`

- Parameters:
	- `weights`: item weights
	- `values`: item values
	- `capacity`: max capacity
- Returns: maximum achievable value

```python
from algonest import knapsack_01

knapsack_01([1, 3, 4], [15, 20, 30], 4)  # 35
```

## Data Structures

### `MinHeap`

- Constructor: `MinHeap()`
- Key methods:
	- `insert(value: Any) -> None`
	- `extract_min() -> Any`
	- `heapify(values: List[Any]) -> None`

```python
from algonest import MinHeap

heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.extract_min()  # 1
```

### `Trie`

- Constructor: `Trie()`
- Key methods:
	- `insert(word: str) -> None`
	- `search(word: str) -> bool`
	- `starts_with(prefix: str) -> bool`
	- `delete(word: str) -> bool`

```python
from algonest import Trie

trie = Trie()
trie.insert("algo")
trie.search("algo")  # True
trie.starts_with("al")  # True
```

### `SegmentTree`

- Constructor: `SegmentTree(values: List[int])`
- Key methods:
	- `point_update(pos: int, value: int) -> None`
	- `range_sum(ql: int, qr: int) -> int`
	- `range_min(ql: int, qr: int) -> int`
	- `range_max(ql: int, qr: int) -> int`

```python
from algonest import SegmentTree

seg = SegmentTree([2, 1, 5, 3])
seg.range_sum(1, 3)  # 9
```

## Utilities

### `validate_iterable(arr: Any) -> List[Any]`

- Parameters:
	- `arr`: any candidate iterable
- Returns: list copy of input

### `run_tests(test_path: str = "tests") -> int`

- Parameters:
	- `test_path`: test target path
- Returns: pytest process exit code

## Local Verification

```bash
python -m pytest -q tests
python benchmarks/compare_algorithms.py
```

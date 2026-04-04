"""Lightweight benchmarks comparing algonest implementations with built-ins."""

from time import perf_counter
from typing import Callable, Dict, List

from algonest import binary_search, merge_sort


def _benchmark_once(func: Callable[[], object]) -> float:
    start = perf_counter()
    func()
    return perf_counter() - start


def compare_search_and_sort(size: int = 10000) -> Dict[str, float]:
    """Return timing snapshot for selected algorithms.

    Args:
        size (int): Dataset size.

    Returns:
        Dict[str, float]: Timing dictionary in seconds.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Example:
        >>> result = compare_search_and_sort(100)
        >>> "algonest_merge_sort" in result
        True
    """
    data = list(range(size))
    target = size // 2

    timings = {
        "algonest_binary_search": _benchmark_once(lambda: binary_search(data, target)),
        "builtin_in_check": _benchmark_once(lambda: (target in data)),
        "algonest_merge_sort": _benchmark_once(lambda: merge_sort(data[::-1])),
        "builtin_sorted": _benchmark_once(lambda: sorted(data[::-1])),
    }

    return timings


if __name__ == "__main__":
    for key, value in compare_search_and_sort().items():
        print(f"{key}: {value:.6f}s")

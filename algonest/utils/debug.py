"""Debugging and instrumentation helpers."""

from time import perf_counter
from typing import Any, Callable, Iterable, Tuple


def time_function(
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> Tuple[Any, float]:
    """Execute function and return its result with elapsed seconds.

    Args:
        func (Callable[..., Any]): Callable to execute.
        *args (Any): Positional arguments for func.
        **kwargs (Any): Keyword arguments for func.

    Returns:
        Tuple[Any, float]: Function result and elapsed wall time in seconds.

    Raises:
        TypeError: If func is not callable.

    Time Complexity: O(f)
    Space Complexity: O(1)

    Example:
        >>> value, elapsed = time_function(sum, [1, 2, 3])
        >>> value
        6
    """
    if not callable(func):
        raise TypeError("func must be callable")

    start = perf_counter()
    result = func(*args, **kwargs)
    elapsed = perf_counter() - start
    return result, elapsed


def assert_sorted(values: Iterable[Any]) -> None:
    """Raise ValueError when iterable values are not non-decreasing.

    Args:
        values (Iterable[Any]): Comparable values.

    Returns:
        None: Validation-only helper.

    Raises:
        ValueError: If values are not sorted.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> assert_sorted([1, 2, 2, 3])
    """
    seq = list(values)
    for index in range(1, len(seq)):
        if seq[index] < seq[index - 1]:
            raise ValueError("values must be sorted in non-decreasing order")

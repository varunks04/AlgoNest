"""Basic statistics utility functions."""

from collections import Counter
from math import sqrt
from typing import Iterable, List


def _to_list(values: Iterable[float]) -> List[float]:
    """Materialize iterable and ensure it is non-empty.

    Args:
        values: Input numeric iterable.

    Returns:
        Materialized list of values.

    Raises:
        ValueError: If input is empty.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    data = list(values)
    if not data:
        raise ValueError("values must be non-empty")
    return data


def mean(values: Iterable[float]) -> float:
    """Compute arithmetic mean.

    Args:
        values: Input numeric iterable.

    Returns:
        Mean value.

    Raises:
        ValueError: If input is empty.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    data = _to_list(values)
    return sum(data) / len(data)


def median(values: Iterable[float]) -> float:
    """Compute median value.

    Args:
        values: Input numeric iterable.

    Returns:
        Median.

    Raises:
        ValueError: If input is empty.

    Time Complexity:
        O(n log n).

    Space Complexity:
        O(n).
    """
    data = sorted(_to_list(values))
    count = len(data)
    middle = count // 2
    if count % 2 == 1:
        return data[middle]
    return (data[middle - 1] + data[middle]) / 2.0


def mode(values: Iterable[float]) -> float:
    """Compute mode; for ties returns the smallest mode value.

    Args:
        values: Input numeric iterable.

    Returns:
        Mode value.

    Raises:
        ValueError: If input is empty.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    data = _to_list(values)
    counts = Counter(data)
    best_count = max(counts.values())
    modes = [value for value, cnt in counts.items() if cnt == best_count]
    return min(modes)


def variance(values: Iterable[float], sample: bool = False) -> float:
    """Compute population or sample variance.

    Args:
        values: Input numeric iterable.
        sample: If ``True``, compute sample variance with Bessel correction.

    Returns:
        Variance value.

    Raises:
        ValueError: If input is empty or sample variance has fewer than 2 values.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    data = _to_list(values)
    if sample and len(data) < 2:
        raise ValueError("sample variance requires at least 2 values")

    average = mean(data)
    squared_sum = sum((value - average) ** 2 for value in data)
    denominator = len(data) - 1 if sample else len(data)
    return squared_sum / denominator


def std_deviation(values: Iterable[float], sample: bool = False) -> float:
    """Compute standard deviation.

    Args:
        values: Input numeric iterable.
        sample: If ``True``, use sample variance.

    Returns:
        Standard deviation.

    Raises:
        ValueError: If input is empty or sample variance has fewer than 2 values.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    return sqrt(variance(values, sample=sample))

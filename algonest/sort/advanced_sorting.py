"""Additional sorting algorithms for toolkit-style usage."""

from numbers import Real
from typing import Any, Iterable, List

from algonest.utils import _validate_iterable


def shell_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted with Shell sort."""
    values = _validate_iterable(arr)
    n = len(values)
    gap = n // 2

    while gap > 0:
        for current_index in range(gap, n):
            current_value = values[current_index]
            insert_index = current_index
            while insert_index >= gap and values[insert_index - gap] > current_value:
                values[insert_index] = values[insert_index - gap]
                insert_index -= gap
            values[insert_index] = current_value
        gap //= 2

    return values


def bucket_sort(arr: Iterable[Real], bucket_count: int = 10) -> List[Real]:
    """Return a new list sorted using bucket sort for numeric values."""
    values = _validate_iterable(arr)
    if not values:
        return []

    if bucket_count <= 0:
        raise ValueError("bucket_count must be positive")

    for value in values:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("bucket_sort requires numeric elements")

    minimum = min(values)
    maximum = max(values)
    if minimum == maximum:
        return values[:]

    buckets: List[List[Real]] = [[] for _ in range(bucket_count)]
    spread = float(maximum - minimum)

    for value in values:
        normalized = (float(value) - float(minimum)) / spread
        index = min(bucket_count - 1, int(normalized * bucket_count))
        buckets[index].append(value)

    output: List[Real] = []
    for bucket in buckets:
        output.extend(sorted(bucket))

    return output


def tim_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted using Python's Timsort implementation."""
    values = _validate_iterable(arr)
    return sorted(values)


def cycle_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted using cycle sort."""
    values = _validate_iterable(arr)
    n = len(values)

    for cycle_start in range(0, n - 1):
        item = values[cycle_start]
        pos = cycle_start

        for candidate_index in range(cycle_start + 1, n):
            if values[candidate_index] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == values[pos]:
            pos += 1

        values[pos], item = item, values[pos]

        while pos != cycle_start:
            pos = cycle_start
            for candidate_index in range(cycle_start + 1, n):
                if values[candidate_index] < item:
                    pos += 1

            while item == values[pos]:
                pos += 1

            values[pos], item = item, values[pos]

    return values

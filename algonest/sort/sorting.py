"""Grouped sorting algorithms for algonest Phase 1."""

from numbers import Integral
from typing import Any, Iterable, List

from algonest.utils import _validate_iterable


RADIX_BASE = 10


def bubble_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted in ascending order using bubble sort.

    Args:
        arr (Iterable[Any]): Iterable input data.

    Returns:
        List[Any]: Sorted list.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Example:
        >>> bubble_sort([3, 1, 2])
        [1, 2, 3]
    """
    values = _validate_iterable(arr)

    for i in range(len(values)):
        swapped = False
        for j in range(0, len(values) - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break

    return values


def selection_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted in ascending order using selection sort.

    Args:
        arr (Iterable[Any]): Iterable input data.

    Returns:
        List[Any]: Sorted list.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Example:
        >>> selection_sort([3, 1, 2])
        [1, 2, 3]
    """
    values = _validate_iterable(arr)

    for i in range(len(values)):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]

    return values


def insertion_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted in ascending order using insertion sort.

    Args:
        arr (Iterable[Any]): Iterable input data.

    Returns:
        List[Any]: Sorted list.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n^2) worst case
    Space Complexity: O(n)

    Example:
        >>> insertion_sort([3, 1, 2])
        [1, 2, 3]
    """
    values = _validate_iterable(arr)

    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key

    return values


def merge_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted in ascending order using merge sort.

    Args:
        arr (Iterable[Any]): Iterable input data.

    Returns:
        List[Any]: Sorted list.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Example:
        >>> merge_sort([3, 1, 2])
        [1, 2, 3]
    """
    values = _validate_iterable(arr)

    def _sort(data: List[Any]) -> List[Any]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = _sort(data[:mid])
        right = _sort(data[mid:])
        merged: List[Any] = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    return _sort(values)


def quick_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted in ascending order using quick sort.

    Args:
        arr (Iterable[Any]): Iterable input data.

    Returns:
        List[Any]: Sorted list.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n log n) average
    Space Complexity: O(n)

    Example:
        >>> quick_sort([3, 1, 2])
        [1, 2, 3]
    """
    values = _validate_iterable(arr)

    def _sort(data: List[Any]) -> List[Any]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        lower = [x for x in data if x < pivot]
        equal = [x for x in data if x == pivot]
        higher = [x for x in data if x > pivot]
        return _sort(lower) + equal + _sort(higher)

    return _sort(values)


def heap_sort(arr: Iterable[Any]) -> List[Any]:
    """Return a new list sorted in ascending order using heap sort.

    Args:
        arr (Iterable[Any]): Iterable input data.

    Returns:
        List[Any]: Sorted list.

    Raises:
        TypeError: If arr is not an iterable.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Example:
        >>> heap_sort([3, 1, 2])
        [1, 2, 3]
    """
    values = _validate_iterable(arr)

    def _heapify(data: List[Any], n: int, root: int) -> None:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right
        if largest != root:
            data[root], data[largest] = data[largest], data[root]
            _heapify(data, n, largest)

    for i in range(len(values) // 2 - 1, -1, -1):
        _heapify(values, len(values), i)

    for i in range(len(values) - 1, 0, -1):
        values[0], values[i] = values[i], values[0]
        _heapify(values, i, 0)

    return values


def counting_sort(arr: Iterable[Any]) -> List[int]:
    """Return a new list sorted in ascending order using counting sort.

    Args:
        arr (Iterable[Any]): Iterable of integer values.

    Returns:
        List[int]: Sorted integer list.

    Raises:
        TypeError: If arr is not iterable or contains non-integers.

    Time Complexity: O(n + k)
    Space Complexity: O(n + k)

    Example:
        >>> counting_sort([4, 1, 3, 1])
        [1, 1, 3, 4]
    """
    values = _validate_iterable(arr)
    if not values:
        return []

    for value in values:
        if not isinstance(value, Integral) or isinstance(value, bool):
            raise TypeError("counting_sort requires integer elements")

    minimum = min(values)
    maximum = max(values)
    counts = [0] * (maximum - minimum + 1)

    for value in values:
        counts[value - minimum] += 1

    output: List[int] = []
    for offset, count in enumerate(counts):
        if count > 0:
            output.extend([minimum + offset] * count)

    return output


def radix_sort(arr: Iterable[Any]) -> List[int]:
    """Return a new list sorted in ascending order using radix sort.

    Args:
        arr (Iterable[Any]): Iterable of non-negative integers.

    Returns:
        List[int]: Sorted integer list.

    Raises:
        TypeError: If arr is not iterable or contains non-integers.
        ValueError: If any element is negative.

    Time Complexity: O(d * (n + k))
    Space Complexity: O(n + k)

    Example:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    values = _validate_iterable(arr)
    if not values:
        return []

    for value in values:
        if not isinstance(value, Integral) or isinstance(value, bool):
            raise TypeError("radix_sort requires integer elements")
        if value < 0:
            raise ValueError("radix_sort supports only non-negative integers")

    output = values[:]
    place = 1
    maximum = max(output)

    while maximum // place > 0:
        counts = [0] * RADIX_BASE
        for value in output:
            counts[(value // place) % RADIX_BASE] += 1
        for i in range(1, RADIX_BASE):
            counts[i] += counts[i - 1]

        temp = [0] * len(output)
        for i in range(len(output) - 1, -1, -1):
            digit = (output[i] // place) % RADIX_BASE
            counts[digit] -= 1
            temp[counts[digit]] = output[i]

        output = temp
        place *= RADIX_BASE

    return output

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

    for pass_index in range(len(values)):
        swapped = False
        for compare_index in range(0, len(values) - pass_index - 1):
            if values[compare_index] > values[compare_index + 1]:
                values[compare_index], values[compare_index + 1] = (
                    values[compare_index + 1],
                    values[compare_index],
                )
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

    for position_index in range(len(values)):
        min_index = position_index
        for candidate_index in range(position_index + 1, len(values)):
            if values[candidate_index] < values[min_index]:
                min_index = candidate_index
        values[position_index], values[min_index] = values[min_index], values[position_index]

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

    for position_index in range(1, len(values)):
        key_value = values[position_index]
        insert_index = position_index - 1
        while insert_index >= 0 and values[insert_index] > key_value:
            values[insert_index + 1] = values[insert_index]
            insert_index -= 1
        values[insert_index + 1] = key_value

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
        middle_index = len(data) // 2
        left = _sort(data[:middle_index])
        right = _sort(data[middle_index:])
        merged: List[Any] = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
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
        lower = [value for value in data if value < pivot]
        equal = [value for value in data if value == pivot]
        higher = [value for value in data if value > pivot]
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

    for heap_root_index in range(len(values) // 2 - 1, -1, -1):
        _heapify(values, len(values), heap_root_index)

    for end_index in range(len(values) - 1, 0, -1):
        values[0], values[end_index] = values[end_index], values[0]
        _heapify(values, end_index, 0)

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
        for digit_index in range(1, RADIX_BASE):
            counts[digit_index] += counts[digit_index - 1]

        temp = [0] * len(output)
        for output_index in range(len(output) - 1, -1, -1):
            digit = (output[output_index] // place) % RADIX_BASE
            counts[digit] -= 1
            temp[counts[digit]] = output[output_index]

        output = temp
        place *= RADIX_BASE

    return output

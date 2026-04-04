"""Dutch flag partitioning algorithms."""

from typing import Any, Iterable, List

from algonest.utils import _validate_iterable


def sort_three_values(
    arr: Iterable[Any],
    low_value: Any,
    mid_value: Any,
    high_value: Any,
) -> List[Any]:
    """Return values sorted by low/mid/high categories in one pass.

    Args:
        arr (Iterable[Any]): Iterable containing only three category values.
        low_value (Any): Category that should appear first.
        mid_value (Any): Category that should appear second.
        high_value (Any): Category that should appear third.

    Returns:
        List[Any]: Newly sorted list by category order.

    Raises:
        TypeError: If arr is not iterable.
        ValueError: If arr contains values outside the three categories.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> sort_three_values([2, 0, 1, 2, 1, 0], 0, 1, 2)
        [0, 0, 1, 1, 2, 2]
    """
    values = _validate_iterable(arr)
    allowed = {low_value, mid_value, high_value}
    for value in values:
        if value not in allowed:
            raise ValueError("arr must contain only the three provided values")

    out = values[:]
    low = 0
    mid = 0
    high = len(out) - 1
    while mid <= high:
        if out[mid] == low_value:
            out[low], out[mid] = out[mid], out[low]
            low += 1
            mid += 1
        elif out[mid] == mid_value:
            mid += 1
        else:
            out[mid], out[high] = out[high], out[mid]
            high -= 1
    return out


def partition_by_pivot(arr: Iterable[Any], pivot: Any) -> List[Any]:
    """Return values partitioned into < pivot, == pivot, > pivot.

    Args:
        arr (Iterable[Any]): Iterable input values.
        pivot (Any): Pivot for partitioning.

    Returns:
        List[Any]: Partitioned list.

    Raises:
        TypeError: If arr is not iterable.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> partition_by_pivot([3, 5, 2, 5, 1], 3)
        [2, 1, 3, 5, 5]
    """
    values = _validate_iterable(arr)
    lower: List[Any] = []
    equal: List[Any] = []
    higher: List[Any] = []

    for value in values:
        if value < pivot:
            lower.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            higher.append(value)

    return lower + equal + higher

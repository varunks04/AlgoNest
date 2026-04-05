"""Permutation utility helpers."""

from typing import Iterable, List, TypeVar

from algonest.utils import _validate_iterable

ValueType = TypeVar("ValueType")


def next_permutation(arr: Iterable[ValueType]) -> List[ValueType]:
    """Return next lexicographic permutation.

    If no greater permutation exists, returns the smallest permutation.
    """
    values: List[ValueType] = _validate_iterable(arr)
    if len(values) <= 1:
        return values

    pivot_index = len(values) - 2
    while pivot_index >= 0 and values[pivot_index] >= values[pivot_index + 1]:
        pivot_index -= 1

    if pivot_index >= 0:
        successor_index = len(values) - 1
        while values[successor_index] <= values[pivot_index]:
            successor_index -= 1
        values[pivot_index], values[successor_index] = (
            values[successor_index],
            values[pivot_index],
        )

    values[pivot_index + 1 :] = reversed(values[pivot_index + 1 :])
    return values


def prev_permutation(arr: Iterable[ValueType]) -> List[ValueType]:
    """Return previous lexicographic permutation.

    If no smaller permutation exists, returns the largest permutation.
    """
    values: List[ValueType] = _validate_iterable(arr)
    if len(values) <= 1:
        return values

    pivot_index = len(values) - 2
    while pivot_index >= 0 and values[pivot_index] <= values[pivot_index + 1]:
        pivot_index -= 1

    if pivot_index >= 0:
        predecessor_index = len(values) - 1
        while values[predecessor_index] >= values[pivot_index]:
            predecessor_index -= 1
        values[pivot_index], values[predecessor_index] = (
            values[predecessor_index],
            values[pivot_index],
        )

    values[pivot_index + 1 :] = reversed(values[pivot_index + 1 :])
    return values

"""Array and string reversal helpers."""

from typing import Iterable, List, TypeVar

from algonest.utils import _validate_iterable

ValueType = TypeVar("ValueType")


def reverse_array(arr: Iterable[ValueType]) -> List[ValueType]:
    """Return reversed array copy."""
    values: List[ValueType] = _validate_iterable(arr)
    return values[::-1]


def reverse_subarray(
    arr: Iterable[ValueType], left: int, right: int
) -> List[ValueType]:
    """Return array copy with inclusive segment [left, right] reversed."""
    values: List[ValueType] = _validate_iterable(arr)
    if left < 0 or right >= len(values) or left > right:
        raise IndexError("left/right must define a valid inclusive range")
    values[left : right + 1] = reversed(values[left : right + 1])
    return values


def reverse_words(text: str) -> str:
    """Return sentence with word order reversed and normalized spaces."""
    if text is None:
        raise TypeError("text must not be None")
    words = text.split()
    return " ".join(reversed(words))

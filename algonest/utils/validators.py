"""Validation helpers shared across algonest package modules."""

from typing import Any, Iterable, List


def validate_iterable(arr: Any) -> List[Any]:
    """Validate iterable input and return list copy.

    Args:
        arr (Any): Input expected to be iterable.

    Returns:
        List[Any]: List copy of input data.

    Raises:
        TypeError: If input is None or non-iterable.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> validate_iterable((1, 2, 3))
        [1, 2, 3]
    """
    if arr is None:
        raise TypeError("Input must not be None")

    try:
        return list(arr)
    except TypeError as exc:
        raise TypeError("Input must be iterable") from exc


def _validate_iterable(arr: Any) -> List[Any]:
    """Backward-compatible alias for existing modules."""
    return validate_iterable(arr)

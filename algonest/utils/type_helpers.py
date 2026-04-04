"""Common type helper aliases for generic algorithm signatures."""

from typing import TypeVar

NumberT = TypeVar("NumberT", int, float)
ComparableT = TypeVar("ComparableT", int, float, str)

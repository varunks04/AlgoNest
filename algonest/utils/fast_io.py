"""Fast I/O helpers for competitive-style workflows."""

from io import StringIO
from typing import Iterable, List


def read_ints_from_text(text: str) -> List[int]:
    """Parse all integers from plain text input.

    Args:
        text (str): Input text containing whitespace-separated integers.

    Returns:
        List[int]: Parsed integers in order.

    Raises:
        TypeError: If text is not a string.
        ValueError: If any token cannot be converted to int.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> read_ints_from_text("1 2 3")
        [1, 2, 3]
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        return []

    return [int(token) for token in text.split()]


def write_lines(lines: Iterable[str]) -> str:
    """Build newline-delimited text from iterable of strings.

    Args:
        lines (Iterable[str]): Lines to write.

    Returns:
        str: Combined text ending with a trailing newline when non-empty.

    Raises:
        TypeError: If lines is not iterable or contains non-string values.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> write_lines(["a", "b"])
        'a\nb\n'
    """
    if lines is None:
        raise TypeError("lines must be an iterable of strings")

    buffer = StringIO()
    count = 0
    for line in lines:
        if not isinstance(line, str):
            raise TypeError("lines must contain only strings")
        buffer.write(line)
        buffer.write("\n")
        count += 1

    return buffer.getvalue() if count > 0 else ""

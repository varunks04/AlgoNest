"""High-utility string helpers grouped for practical package structure."""

from __future__ import annotations


def rolling_hash(text: str, base: int = 257, mod: int = 1_000_000_007) -> int:
    """Compute a polynomial rolling hash for a string.

    Args:
        text: Input text.
        base: Polynomial base multiplier. Must be positive.
        mod: Modulus. Must be positive.

    Returns:
        Hash value in ``[0, mod)``.

    Raises:
        ValueError: If ``base`` or ``mod`` is non-positive.

    Time Complexity:
        O(n), where n is ``len(text)``.

    Space Complexity:
        O(1).
    """
    if base <= 0 or mod <= 0:
        raise ValueError("base and mod must be positive")

    hash_value = 0
    for character in text:
        hash_value = (hash_value * base + ord(character)) % mod
    return hash_value


def is_palindrome(text: str) -> bool:
    """Check whether a string is a palindrome after alphanumeric normalization.

    Args:
        text: Input text.

    Returns:
        ``True`` if normalized text is a palindrome, else ``False``.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n) for normalized characters.
    """
    normalized = [character.lower() for character in text if character.isalnum()]
    return normalized == normalized[::-1]


def longest_palindromic_substring(text: str) -> str:
    """Find the longest palindromic substring using center expansion.

    Args:
        text: Input text.

    Returns:
        The longest palindromic substring. Empty string for empty input.

    Time Complexity:
        O(n^2) in the worst case.

    Space Complexity:
        O(1) auxiliary space.
    """
    if not text:
        return ""

    best_start = 0
    best_length = 1

    def _expand(left: int, right: int) -> None:
        nonlocal best_start, best_length
        while left >= 0 and right < len(text) and text[left] == text[right]:
            current_length = right - left + 1
            if current_length > best_length:
                best_start = left
                best_length = current_length
            left -= 1
            right += 1

    for center in range(len(text)):
        _expand(center, center)
        _expand(center, center + 1)

    return text[best_start : best_start + best_length]

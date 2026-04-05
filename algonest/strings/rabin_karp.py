"""Rabin-Karp rolling hash string matching."""

from typing import List


def rabin_karp_search(text: str, pattern: str) -> List[int]:
    """Return all pattern match starting indices using rolling hash.

    Args:
        text: Input text to search.
        pattern: Pattern to match.

    Returns:
        Sorted list of match start indices.

    Time Complexity:
        O(len(text) + len(pattern)) average.

    Space Complexity:
        O(1) auxiliary.
    """
    if pattern == "":
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []

    base = 256
    modulus = 10**9 + 7
    pattern_length = len(pattern)
    highest_power = pow(base, pattern_length - 1, modulus)

    pattern_hash = 0
    window_hash = 0
    for index in range(pattern_length):
        pattern_hash = (pattern_hash * base + ord(pattern[index])) % modulus
        window_hash = (window_hash * base + ord(text[index])) % modulus

    matches: List[int] = []
    for start_index in range(len(text) - pattern_length + 1):
        if (
            pattern_hash == window_hash
            and text[start_index : start_index + pattern_length] == pattern
        ):
            matches.append(start_index)

        next_index = start_index + pattern_length
        if next_index < len(text):
            window_hash = (
                window_hash - ord(text[start_index]) * highest_power
            ) % modulus
            window_hash = (window_hash * base + ord(text[next_index])) % modulus
    return matches

"""Z-algorithm string processing."""

from typing import List


def z_array(text: str) -> List[int]:
    """Compute Z-array for a string.

    Args:
        text: Input string.

    Returns:
        Z-array where each index stores longest prefix match length.

    Time Complexity:
        O(len(text)).

    Space Complexity:
        O(len(text)).
    """
    n = len(text)
    z_values = [0] * n
    left = 0
    right = 0
    for index in range(1, n):
        if index <= right:
            z_values[index] = min(right - index + 1, z_values[index - left])
        while (
            index + z_values[index] < n
            and text[z_values[index]] == text[index + z_values[index]]
        ):
            z_values[index] += 1
        if index + z_values[index] - 1 > right:
            left = index
            right = index + z_values[index] - 1
    return z_values


def z_search(text: str, pattern: str) -> List[int]:
    """Find all occurrences of pattern in text using Z-algorithm.

    Args:
        text: Input text to search.
        pattern: Pattern to match.

    Returns:
        Sorted list of match start indices.

    Time Complexity:
        O(len(text) + len(pattern)).

    Space Complexity:
        O(len(text) + len(pattern)).
    """
    if pattern == "":
        return list(range(len(text) + 1))
    merged_text = pattern + "$" + text
    z_values = z_array(merged_text)
    matches: List[int] = []
    pattern_length = len(pattern)
    for merged_index in range(pattern_length + 1, len(merged_text)):
        if z_values[merged_index] == pattern_length:
            matches.append(merged_index - pattern_length - 1)
    return matches

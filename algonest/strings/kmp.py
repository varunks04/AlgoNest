"""Knuth-Morris-Pratt string matching."""

from typing import List


def kmp_search(text: str, pattern: str) -> List[int]:
    """Return all pattern match starting indices in a text.

    Args:
        text: Input text to search.
        pattern: Pattern to match.

    Returns:
        Sorted list of match start indices.

    Time Complexity:
        O(len(text) + len(pattern)).

    Space Complexity:
        O(len(pattern)).
    """
    if pattern == "":
        return list(range(len(text) + 1))

    lps = [0] * len(pattern)
    prefix_length = 0
    pattern_index = 1
    while pattern_index < len(pattern):
        if pattern[pattern_index] == pattern[prefix_length]:
            prefix_length += 1
            lps[pattern_index] = prefix_length
            pattern_index += 1
        elif prefix_length != 0:
            prefix_length = lps[prefix_length - 1]
        else:
            lps[pattern_index] = 0
            pattern_index += 1

    matches: List[int] = []
    text_index = 0
    pattern_index = 0
    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
            if pattern_index == len(pattern):
                matches.append(text_index - pattern_index)
                pattern_index = lps[pattern_index - 1]
        elif pattern_index != 0:
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1
    return matches

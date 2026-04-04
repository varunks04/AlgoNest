"""Anagram-related string utilities."""

from collections import defaultdict
from typing import Dict, List


def is_anagram(first: str, second: str) -> bool:
    """Return whether two strings are anagrams."""
    if len(first) != len(second):
        return False
    counts: Dict[str, int] = {}
    for ch in first:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in second:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True


def group_anagrams(words: List[str]) -> List[List[str]]:
    """Group words by anagram signature."""
    groups: Dict[tuple[str, ...], List[str]] = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def find_all_anagrams(text: str, pattern: str) -> List[int]:
    """Return start indices of all anagram matches of pattern in text."""
    if len(pattern) > len(text):
        return []

    need: Dict[str, int] = {}
    window: Dict[str, int] = {}
    for ch in pattern:
        need[ch] = need.get(ch, 0) + 1

    out: List[int] = []
    left = 0
    for right, ch in enumerate(text):
        window[ch] = window.get(ch, 0) + 1
        if right - left + 1 > len(pattern):
            left_ch = text[left]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            left += 1
        if right - left + 1 == len(pattern) and window == need:
            out.append(left)

    return out

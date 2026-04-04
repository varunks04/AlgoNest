"""Rabin-Karp rolling hash string matching."""

from typing import List


def rabin_karp_search(text: str, pattern: str) -> List[int]:
    """Return all start indices where pattern appears in text."""
    if pattern == "":
        return list(range(len(text) + 1))
    if len(pattern) > len(text):
        return []

    base = 256
    mod = 10**9 + 7
    m = len(pattern)
    high = pow(base, m - 1, mod)

    p_hash = 0
    w_hash = 0
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        w_hash = (w_hash * base + ord(text[i])) % mod

    out: List[int] = []
    for i in range(len(text) - m + 1):
        if p_hash == w_hash and text[i : i + m] == pattern:
            out.append(i)
        if i + m < len(text):
            w_hash = (w_hash - ord(text[i]) * high) % mod
            w_hash = (w_hash * base + ord(text[i + m])) % mod
    return out

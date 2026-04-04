"""Z-algorithm string processing."""

from typing import List


def z_array(s: str) -> List[int]:
    """Return Z-array for string s."""
    n = len(s)
    z = [0] * n
    left = 0
    right = 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    return z


def z_search(text: str, pattern: str) -> List[int]:
    """Return match indices using Z-algorithm."""
    if pattern == "":
        return list(range(len(text) + 1))
    concat = pattern + "$" + text
    z = z_array(concat)
    out: List[int] = []
    p_len = len(pattern)
    for i in range(p_len + 1, len(concat)):
        if z[i] == p_len:
            out.append(i - p_len - 1)
    return out

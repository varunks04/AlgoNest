"""GCD/LCM and extended Euclidean algorithms."""

from typing import Tuple


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of a and b."""
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Return (g, x, y) such that ax + by = g = gcd(a, b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t

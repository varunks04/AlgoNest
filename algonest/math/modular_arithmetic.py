"""Modular arithmetic utilities."""

from typing import List

from algonest.math.gcd_lcm import extended_gcd


def mod_exp(base: int, exp: int, mod: int) -> int:
    """Return modular exponentiation result."""
    if mod <= 0:
        raise ValueError("mod must be positive")
    result = 1
    value = base % mod
    power = exp
    while power > 0:
        if power & 1:
            result = (result * value) % mod
        value = (value * value) % mod
        power >>= 1
    return result


def mod_inverse(a: int, mod: int) -> int:
    """Return modular inverse of a under mod."""
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % mod


def chinese_remainder_theorem(mods: List[int], rems: List[int]) -> int:
    """Return smallest non-negative solution for CRT system."""
    if len(mods) != len(rems) or not mods:
        raise ValueError("mods and rems must have same non-zero length")

    prod = 1
    for m in mods:
        prod *= m

    result = 0
    for m, r in zip(mods, rems):
        partial = prod // m
        inv = mod_inverse(partial % m, m)
        result += r * partial * inv

    return result % prod

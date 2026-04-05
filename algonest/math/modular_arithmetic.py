"""Modular arithmetic utilities."""

from typing import Sequence

from algonest.math.gcd_lcm import extended_gcd


def mod_exp(base: int, exp: int, mod: int) -> int:
    """Compute modular exponentiation.

    Args:
        base: Base integer.
        exp: Non-negative exponent.
        mod: Positive modulus.

    Returns:
        ``(base ** exp) % mod``.

    Raises:
        ValueError: If ``mod`` is non-positive or ``exp`` is negative.

    Time Complexity:
        O(log exp).

    Space Complexity:
        O(1).
    """
    if mod <= 0:
        raise ValueError("mod must be positive")
    if exp < 0:
        raise ValueError("exp must be non-negative")

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
    """Compute multiplicative inverse of ``a`` modulo ``mod``.

    Args:
        a: Integer to invert.
        mod: Positive modulus.

    Returns:
        ``x`` such that ``(a * x) % mod == 1``.

    Raises:
        ValueError: If modulus is non-positive or inverse does not exist.

    Time Complexity:
        O(log mod).

    Space Complexity:
        O(1).
    """
    if mod <= 0:
        raise ValueError("mod must be positive")

    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % mod


def chinese_remainder_theorem(mods: Sequence[int], rems: Sequence[int]) -> int:
    """Solve a system of congruences using the Chinese Remainder Theorem.

    Args:
        mods: Pairwise coprime positive moduli.
        rems: Remainders aligned with ``mods``.

    Returns:
        Smallest non-negative solution.

    Raises:
        ValueError: If input lengths mismatch/empty, moduli are non-positive, or
            moduli are not pairwise coprime.

    Time Complexity:
        O(n^2 * log M), where M is modulus magnitude.

    Space Complexity:
        O(1) auxiliary (excluding input storage).
    """
    if len(mods) != len(rems) or not mods:
        raise ValueError("mods and rems must have same non-zero length")
    if any(mod <= 0 for mod in mods):
        raise ValueError("all moduli must be positive")

    for left_index in range(len(mods)):
        for right_index in range(left_index + 1, len(mods)):
            if extended_gcd(mods[left_index], mods[right_index])[0] != 1:
                raise ValueError("CRT requires pairwise coprime moduli")

    prod = 1
    for modulus in mods:
        prod *= modulus

    result = 0
    for modulus, remainder in zip(mods, rems):
        partial = prod // modulus
        inv = mod_inverse(partial % modulus, modulus)
        result += remainder * partial * inv

    return result % prod

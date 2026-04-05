"""GCD/LCM and extended Euclidean algorithms."""

from typing import Tuple


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Non-negative greatest common divisor.

    Time Complexity:
        O(log(min(|a|, |b|))).

    Space Complexity:
        O(1).
    """
    first_abs = abs(a)
    second_abs = abs(b)
    while second_abs != 0:
        first_abs, second_abs = second_abs, first_abs % second_abs
    return first_abs


def lcm(a: int, b: int) -> int:
    """Compute the least common multiple.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Non-negative least common multiple, or ``0`` if either value is ``0``.

    Time Complexity:
        O(log(min(|a|, |b|))).

    Space Complexity:
        O(1).
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Run the extended Euclidean algorithm.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Tuple ``(g, x, y)`` such that ``a*x + b*y = g`` and ``g = gcd(a, b)``.

    Time Complexity:
        O(log(min(|a|, |b|))).

    Space Complexity:
        O(1).
    """
    old_remainder, remainder = a, b
    old_coefficient_a, coefficient_a = 1, 0
    old_coefficient_b, coefficient_b = 0, 1
    while remainder != 0:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_coefficient_a, coefficient_a = (
            coefficient_a,
            old_coefficient_a - quotient * coefficient_a,
        )
        old_coefficient_b, coefficient_b = (
            coefficient_b,
            old_coefficient_b - quotient * coefficient_b,
        )
    if old_remainder < 0:
        return -old_remainder, -old_coefficient_a, -old_coefficient_b
    return old_remainder, old_coefficient_a, old_coefficient_b

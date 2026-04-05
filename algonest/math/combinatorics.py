"""Combinatorics utility functions."""

import math


def factorial(n: int) -> int:
    """Compute factorial of a non-negative integer.

    Args:
        n: Non-negative integer.

    Returns:
        ``n!``.

    Raises:
        ValueError: If ``n`` is negative.

    Time Complexity:
        O(n).

    Space Complexity:
        O(1) auxiliary.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return math.factorial(n)


def n_choose_r(n: int, r: int) -> int:
    """Compute binomial coefficient ``C(n, r)``.

    Args:
        n: Population size.
        r: Selection size.

    Returns:
        Number of combinations, or ``0`` for invalid ranges.

    Time Complexity:
        O(min(r, n-r)).

    Space Complexity:
        O(1).
    """
    if n < 0 or r < 0 or r > n:
        return 0
    return math.comb(n, r)


def permutations_count(n: int, r: int) -> int:
    """Compute permutation count ``P(n, r)``.

    Args:
        n: Population size.
        r: Selection length.

    Returns:
        Number of ordered selections, or ``0`` for invalid ranges.

    Time Complexity:
        O(r).

    Space Complexity:
        O(1).
    """
    if n < 0 or r < 0 or r > n:
        return 0
    return math.perm(n, r)


def catalan_number(n: int) -> int:
    """Compute the nth Catalan number.

    Args:
        n: Non-negative index.

    Returns:
        nth Catalan number.

    Raises:
        ValueError: If ``n`` is negative.

    Time Complexity:
        O(n) via combinatorics primitive.

    Space Complexity:
        O(1).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return math.comb(2 * n, n) // (n + 1)

"""Canonical Fibonacci DP patterns."""

from functools import lru_cache


def fib_memo(n: int) -> int:
    """Compute the nth Fibonacci number with memoized recursion.

    Args:
        n: Sequence index, zero-based.

    Returns:
        nth Fibonacci number.

    Raises:
        ValueError: If ``n`` is negative.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    @lru_cache(maxsize=None)
    def _fib(index: int) -> int:
        if index < 2:
            return index
        return _fib(index - 1) + _fib(index - 2)

    return _fib(n)


def fib_tabulated(n: int) -> int:
    """Compute the nth Fibonacci number with bottom-up tabulation.

    Args:
        n: Sequence index, zero-based.

    Returns:
        nth Fibonacci number.

    Raises:
        ValueError: If ``n`` is negative.

    Time Complexity:
        O(n).

    Space Complexity:
        O(n).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    return dp[n]


def fib_space_optimized(n: int) -> int:
    """Compute the nth Fibonacci number with O(1) auxiliary space.

    Args:
        n: Sequence index, zero-based.

    Returns:
        nth Fibonacci number.

    Raises:
        ValueError: If ``n`` is negative.

    Time Complexity:
        O(n).

    Space Complexity:
        O(1).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1

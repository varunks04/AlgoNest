"""Prime number utilities using sieve and factorization."""

from typing import List


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Generate all prime numbers up to ``limit`` (inclusive).

    Args:
        limit: Upper bound.

    Returns:
        Sorted list of prime numbers ``<= limit``.

    Raises:
        ValueError: If ``limit`` is negative.

    Time Complexity:
        O(limit log log limit).

    Space Complexity:
        O(limit).
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    prime_candidate = 2
    while prime_candidate * prime_candidate <= limit:
        if is_prime[prime_candidate]:
            for multiple in range(
                prime_candidate * prime_candidate, limit + 1, prime_candidate
            ):
                is_prime[multiple] = False
        prime_candidate += 1
    return [index for index, prime in enumerate(is_prime) if prime]


def is_prime(n: int) -> bool:
    """Check primality of an integer.

    Args:
        n: Integer to test.

    Returns:
        ``True`` if ``n`` is prime.

    Time Complexity:
        O(sqrt(n)).

    Space Complexity:
        O(1).
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def prime_factors(n: int) -> List[int]:
    """Factorize an integer into prime factors with repetition.

    Args:
        n: Integer to factorize.

    Returns:
        Prime factors in non-decreasing order.

    Raises:
        ValueError: If ``n`` is less than ``2``.

    Time Complexity:
        O(sqrt(n)) in worst case.

    Space Complexity:
        O(k), where k is number of prime factors.
    """
    if n < 2:
        raise ValueError("n must be >= 2")

    factors: List[int] = []
    value = n
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors

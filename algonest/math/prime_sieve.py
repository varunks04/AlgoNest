"""Prime number utilities using sieve and factorization."""

from typing import List


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Return list of primes up to limit inclusive."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1
    return [i for i, prime in enumerate(is_prime) if prime]


def is_prime(n: int) -> bool:
    """Return whether n is prime."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factors(n: int) -> List[int]:
    """Return prime factors of n with repetition."""
    factors: List[int] = []
    value = n
    d = 2
    while d * d <= value:
        while value % d == 0:
            factors.append(d)
            value //= d
        d += 1
    if value > 1:
        factors.append(value)
    return factors

from algonest.math import is_prime, prime_factors, sieve_of_eratosthenes


def test_prime_utilities() -> None:
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert is_prime(29) is True
    assert prime_factors(84) == [2, 2, 3, 7]

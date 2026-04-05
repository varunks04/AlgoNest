"""Consolidated tests for math utilities."""

import pytest

from algonest.math import (
    catalan_number,
    chinese_remainder_theorem,
    clear_bit,
    count_bits,
    factorial,
    fast_power,
    gcd,
    identity,
    is_power_of_two,
    is_prime,
    lcm,
    matrix_multiply,
    matrix_power,
    mean,
    median,
    mod_exp,
    mod_inverse,
    mode,
    n_choose_r,
    permutations_count,
    prime_factors,
    set_bit,
    sieve_of_eratosthenes,
    std_deviation,
    variance,
    xor_trick,
)


def test_bit_manipulation_happy_path() -> None:
    assert count_bits(13) == 3
    assert is_power_of_two(16) is True
    assert set_bit(8, 0) == 9
    assert clear_bit(9, 0) == 8
    assert xor_trick(5, 3) == 6


def test_bit_manipulation_raises_on_invalid_bit_position() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        set_bit(1, -1)
    with pytest.raises(ValueError, match="non-negative"):
        clear_bit(1, -1)


def test_fast_power_happy_path() -> None:
    assert fast_power(2, 10) == 1024


def test_gcd_lcm_happy_path() -> None:
    assert gcd(54, 24) == 6
    assert lcm(6, 8) == 24


def test_modular_arithmetic_happy_path() -> None:
    assert mod_exp(2, 10, 1000) == 24
    assert mod_inverse(3, 11) == 4
    assert chinese_remainder_theorem([3, 5, 7], [2, 3, 2]) == 23


def test_modular_arithmetic_raises_on_invalid_inputs() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        mod_exp(2, -1, 11)
    with pytest.raises(ValueError, match="pairwise coprime"):
        chinese_remainder_theorem([4, 6], [1, 2])


def test_prime_helpers_happy_path() -> None:
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert is_prime(29) is True
    assert prime_factors(84) == [2, 2, 3, 7]


def test_prime_helpers_raise_on_invalid_inputs() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        sieve_of_eratosthenes(-1)
    with pytest.raises(ValueError, match=">= 2"):
        prime_factors(1)


def test_combinatorics_helpers_happy_path() -> None:
    assert factorial(5) == 120
    assert n_choose_r(5, 2) == 10
    assert permutations_count(5, 2) == 20
    assert catalan_number(3) == 5


def test_combinatorics_helpers_edge_cases() -> None:
    assert n_choose_r(3, 5) == 0
    assert permutations_count(3, 5) == 0
    with pytest.raises(ValueError, match="non-negative"):
        factorial(-1)


def test_matrix_math_helpers_happy_path() -> None:
    assert identity(2) == [[1, 0], [0, 1]]
    assert matrix_multiply([[1, 2]], [[3], [4]]) == [[11]]
    assert matrix_power([[1, 1], [1, 0]], 2) == [[2, 1], [1, 1]]


def test_statistics_helpers_happy_path() -> None:
    values = [1, 2, 2, 3]
    assert mean(values) == 2.0
    assert median(values) == 2.0
    assert mode(values) == 2
    assert variance(values) == 0.5
    assert round(std_deviation(values), 6) == round(0.7071067811865476, 6)

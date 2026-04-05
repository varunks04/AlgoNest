"""Math package for specialized algorithms."""

from algonest.math.bit_manipulation import (
    clear_bit,
    count_bits,
    is_power_of_two,
    set_bit,
    xor_trick,
)
from algonest.math.combinatorics import catalan_number, factorial, n_choose_r, permutations_count
from algonest.math.fast_power import fast_power
from algonest.math.gcd_lcm import extended_gcd, gcd, lcm
from algonest.math.matrix_math import identity, matrix_multiply, matrix_power
from algonest.math.modular_arithmetic import chinese_remainder_theorem, mod_exp, mod_inverse
from algonest.math.prime_sieve import is_prime, prime_factors, sieve_of_eratosthenes
from algonest.math.statistics import mean, median, mode, std_deviation, variance

__all__ = [
    "gcd",
    "lcm",
    "extended_gcd",
    "sieve_of_eratosthenes",
    "is_prime",
    "prime_factors",
    "mod_exp",
    "mod_inverse",
    "chinese_remainder_theorem",
    "fast_power",
    "count_bits",
    "is_power_of_two",
    "set_bit",
    "clear_bit",
    "xor_trick",
    "factorial",
    "n_choose_r",
    "permutations_count",
    "catalan_number",
    "identity",
    "matrix_multiply",
    "matrix_power",
    "mean",
    "median",
    "mode",
    "variance",
    "std_deviation",
]

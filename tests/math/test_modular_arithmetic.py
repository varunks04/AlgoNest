from algonest.math import chinese_remainder_theorem, mod_exp, mod_inverse


def test_modular_arithmetic() -> None:
    assert mod_exp(2, 10, 1000) == 24
    assert mod_inverse(3, 11) == 4
    assert chinese_remainder_theorem([3, 5, 7], [2, 3, 2]) == 23

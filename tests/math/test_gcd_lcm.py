from algonest.math import extended_gcd, gcd, lcm


def test_gcd_lcm_extended() -> None:
    assert gcd(54, 24) == 6
    assert lcm(6, 8) == 24
    g, x, y = extended_gcd(30, 12)
    assert g == 6 and 30 * x + 12 * y == g

from algonest.math import fast_power


def test_fast_power() -> None:
    assert fast_power(2, 10) == 1024

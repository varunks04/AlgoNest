from algonest.math import clear_bit, count_bits, is_power_of_two, set_bit, xor_trick


def test_bit_manipulation() -> None:
    assert count_bits(13) == 3
    assert is_power_of_two(16) is True
    assert set_bit(8, 0) == 9
    assert clear_bit(9, 0) == 8
    assert xor_trick(5, 3) == 6

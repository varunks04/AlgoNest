"""Common bit-manipulation utilities."""


def count_bits(value: int) -> int:
    """Return number of set bits in integer."""
    if value < 0:
        raise ValueError("value must be non-negative")
    count = 0
    current = value
    while current > 0:
        current &= current - 1
        count += 1
    return count


def is_power_of_two(value: int) -> bool:
    """Return whether value is power of two."""
    return value > 0 and (value & (value - 1)) == 0


def set_bit(value: int, pos: int) -> int:
    """Return value with bit at pos set to 1."""
    return value | (1 << pos)


def clear_bit(value: int, pos: int) -> int:
    """Return value with bit at pos cleared to 0."""
    return value & ~(1 << pos)


def xor_trick(a: int, b: int) -> int:
    """Return XOR of two integers."""
    return a ^ b

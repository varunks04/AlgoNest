"""Common bit-manipulation utilities."""


def count_bits(value: int) -> int:
    """Count set bits in a non-negative integer.

    Args:
        value: Integer value.

    Returns:
        Number of 1-bits in binary representation.

    Raises:
        ValueError: If ``value`` is negative.

    Time Complexity:
        O(k), where k is number of set bits.

    Space Complexity:
        O(1).
    """
    if value < 0:
        raise ValueError("value must be non-negative")
    count = 0
    current = value
    while current > 0:
        current &= current - 1
        count += 1
    return count


def is_power_of_two(value: int) -> bool:
    """Check whether a value is an exact power of two.

    Args:
        value: Integer value.

    Returns:
        ``True`` if ``value`` is a positive power of two.

    Time Complexity:
        O(1).

    Space Complexity:
        O(1).
    """
    return value > 0 and (value & (value - 1)) == 0


def set_bit(value: int, pos: int) -> int:
    """Set a bit at a given position.

    Args:
        value: Source integer.
        pos: Zero-based bit position.

    Returns:
        Integer with the bit at ``pos`` set.

    Raises:
        ValueError: If ``pos`` is negative.

    Time Complexity:
        O(1).

    Space Complexity:
        O(1).
    """
    if pos < 0:
        raise ValueError("pos must be non-negative")
    return value | (1 << pos)


def clear_bit(value: int, pos: int) -> int:
    """Clear a bit at a given position.

    Args:
        value: Source integer.
        pos: Zero-based bit position.

    Returns:
        Integer with the bit at ``pos`` cleared.

    Raises:
        ValueError: If ``pos`` is negative.

    Time Complexity:
        O(1).

    Space Complexity:
        O(1).
    """
    if pos < 0:
        raise ValueError("pos must be non-negative")
    return value & ~(1 << pos)


def xor_trick(a: int, b: int) -> int:
    """Compute bitwise XOR of two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Bitwise XOR result.

    Time Complexity:
        O(1).

    Space Complexity:
        O(1).
    """
    return a ^ b

"""Binary exponentiation utility."""


def fast_power(base: int, exp: int) -> int:
    """Raise an integer base to a non-negative integer exponent.

    Args:
        base: Integer base.
        exp: Non-negative exponent.

    Returns:
        ``base`` raised to ``exp``.

    Raises:
        ValueError: If ``exp`` is negative.

    Time Complexity:
        O(log exp).

    Space Complexity:
        O(1).
    """
    if exp < 0:
        raise ValueError("exp must be non-negative")
    result = 1
    value = base
    power = exp
    while power > 0:
        if power & 1:
            result *= value
        value *= value
        power >>= 1
    return result

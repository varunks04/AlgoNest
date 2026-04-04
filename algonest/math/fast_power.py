"""Binary exponentiation utility."""


def fast_power(base: int, exp: int) -> int:
    """Return base raised to exp using binary exponentiation."""
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

"""Coin change dynamic programming algorithms."""

from typing import Sequence


def min_coins(coins: Sequence[int], amount: int) -> int:
    """Compute the minimum number of coins needed to make a target amount.

    Args:
        coins: Available coin denominations. Each coin must be a positive integer.
        amount: Target amount to form.

    Returns:
        The fewest number of coins required, or ``-1`` if the amount is not
        constructible.

    Raises:
        ValueError: If ``amount`` is negative or any coin is non-positive.

    Time Complexity:
        O(amount * len(coins)).

    Space Complexity:
        O(amount).
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coins must contain only positive values")

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return -1 if dp[amount] > amount else int(dp[amount])


def coin_change_ways(coins: Sequence[int], amount: int) -> int:
    """Count combinations to form a target amount using unlimited coins.

    Args:
        coins: Available coin denominations. Each coin must be a positive integer.
        amount: Target amount to form.

    Returns:
        Number of unique denomination combinations.

    Raises:
        ValueError: If ``amount`` is negative or any coin is non-positive.

    Time Complexity:
        O(amount * len(coins)).

    Space Complexity:
        O(amount).
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coins must contain only positive values")

    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]
    return int(dp[amount])

"""Coin change dynamic programming algorithms."""

from typing import List


def min_coins(coins: List[int], amount: int) -> int:
    """Return minimum number of coins to form amount, or -1 if impossible."""
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return -1 if dp[amount] > amount else dp[amount]


def coin_change_ways(coins: List[int], amount: int) -> int:
    """Return number of ways to form amount using unlimited coins."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]
    return dp[amount]

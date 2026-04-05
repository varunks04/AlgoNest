"""Longest common subsequence algorithms."""


def lcs_length(first: str, second: str) -> int:
    """Compute the longest common subsequence length.

    Args:
        first: First input string.
        second: Second input string.

    Returns:
        LCS length.

    Time Complexity:
        O(len(first) * len(second)).

    Space Complexity:
        O(len(first) * len(second)).
    """
    first_length = len(first)
    n = len(second)
    dp = [[0] * (n + 1) for _ in range(first_length + 1)]

    for first_index in range(1, first_length + 1):
        for second_index in range(1, n + 1):
            if first[first_index - 1] == second[second_index - 1]:
                dp[first_index][second_index] = dp[first_index - 1][second_index - 1] + 1
            else:
                dp[first_index][second_index] = max(
                    dp[first_index - 1][second_index],
                    dp[first_index][second_index - 1],
                )

    return int(dp[first_length][n])

"""Edit distance (Levenshtein) algorithm."""


def edit_distance(first: str, second: str) -> int:
    """Compute Levenshtein edit distance between two strings.

    Args:
        first: Source string.
        second: Target string.

    Returns:
        The minimum number of insertions, deletions, and substitutions needed
        to transform ``first`` into ``second``.

    Time Complexity:
        O(len(first) * len(second)).

    Space Complexity:
        O(len(first) * len(second)).
    """
    first_length = len(first)
    n = len(second)
    dp = [[0] * (n + 1) for _ in range(first_length + 1)]

    for first_index in range(first_length + 1):
        dp[first_index][0] = first_index
    for second_index in range(n + 1):
        dp[0][second_index] = second_index

    for first_index in range(1, first_length + 1):
        for second_index in range(1, n + 1):
            if first[first_index - 1] == second[second_index - 1]:
                dp[first_index][second_index] = dp[first_index - 1][second_index - 1]
            else:
                dp[first_index][second_index] = 1 + min(
                    dp[first_index - 1][second_index],
                    dp[first_index][second_index - 1],
                    dp[first_index - 1][second_index - 1],
                )

    return int(dp[first_length][n])

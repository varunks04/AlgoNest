"""Reusable DP patterns for grid problems."""

from typing import Sequence


def unique_paths(m: int, n: int) -> int:
    """Count unique paths from top-left to bottom-right in an m x n grid.

    Args:
        m: Row count.
        n: Column count.

    Returns:
        Number of unique paths moving only right or down.

    Raises:
        ValueError: If ``m`` or ``n`` is non-positive.

    Time Complexity:
        O(m * n).

    Space Complexity:
        O(n).
    """
    if m <= 0 or n <= 0:
        raise ValueError("m and n must be positive")

    dp = [1] * n
    for _ in range(1, m):
        for col in range(1, n):
            dp[col] += dp[col - 1]
    return int(dp[-1])


def min_path_sum(grid: Sequence[Sequence[int]]) -> int:
    """Compute minimum path sum from top-left to bottom-right.

    Args:
        grid: Rectangular matrix of path costs.

    Returns:
        Minimum achievable path sum using right/down moves.

    Raises:
        ValueError: If grid is empty or not rectangular.

    Time Complexity:
        O(rows * cols).

    Space Complexity:
        O(cols).
    """
    if not grid or not grid[0]:
        raise ValueError("grid must be non-empty")

    rows = len(grid)
    cols = len(grid[0])
    for row in grid:
        if len(row) != cols:
            raise ValueError("grid must be rectangular")

    dp = [0] * cols

    for row_index in range(rows):
        for col_index in range(cols):
            if row_index == 0 and col_index == 0:
                dp[col_index] = grid[row_index][col_index]
            elif row_index == 0:
                dp[col_index] = dp[col_index - 1] + grid[row_index][col_index]
            elif col_index == 0:
                dp[col_index] = dp[col_index] + grid[row_index][col_index]
            else:
                dp[col_index] = (
                    min(dp[col_index], dp[col_index - 1]) + grid[row_index][col_index]
                )

    return int(dp[-1])

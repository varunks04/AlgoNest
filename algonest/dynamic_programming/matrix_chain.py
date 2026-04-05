"""Matrix chain multiplication optimization."""

from typing import Sequence


def matrix_chain_order(dims: Sequence[int]) -> int:
    """Compute minimum scalar multiplications for matrix chain product.

    Args:
        dims: Dimension array of length ``n + 1`` for ``n`` matrices.

    Returns:
        Minimum multiplication cost.

    Raises:
        ValueError: If fewer than two dimensions are provided, or if any
            dimension is non-positive.

    Time Complexity:
        O(n^3), where n is number of matrices.

    Space Complexity:
        O(n^2).
    """
    if len(dims) < 2:
        raise ValueError("dims must contain at least two values")
    if any(value <= 0 for value in dims):
        raise ValueError("dims must contain only positive values")

    matrix_count = len(dims) - 1
    if matrix_count <= 1:
        return 0

    dp = [[0] * matrix_count for _ in range(matrix_count)]

    for chain_length in range(2, matrix_count + 1):
        for start in range(matrix_count - chain_length + 1):
            end = start + chain_length - 1
            dp[start][end] = 10**18
            for split in range(start, end):
                cost = (
                    dp[start][split]
                    + dp[split + 1][end]
                    + dims[start] * dims[split + 1] * dims[end + 1]
                )
                if cost < dp[start][end]:
                    dp[start][end] = cost

    return int(dp[0][matrix_count - 1])

"""Backtracking combination generators."""

from typing import Iterable, List, Sequence


def combinations(values: Sequence[int], k: int) -> List[List[int]]:
    """Return all size-k combinations."""
    if k < 0:
        raise ValueError("k must be non-negative")

    nums = list(values)
    output: List[List[int]] = []

    def _dfs(start: int, path: List[int]) -> None:
        if len(path) == k:
            output.append(path[:])
            return
        for candidate_index in range(start, len(nums)):
            path.append(nums[candidate_index])
            _dfs(candidate_index + 1, path)
            path.pop()

    _dfs(0, [])
    return output


def combination_sum(values: Iterable[int], target: int) -> List[List[int]]:
    """Return combinations where values can be reused to hit target."""
    nums = sorted([v for v in values if v > 0])
    output: List[List[int]] = []

    def _dfs(start: int, remain: int, path: List[int]) -> None:
        if remain == 0:
            output.append(path[:])
            return
        for candidate_index in range(start, len(nums)):
            value = nums[candidate_index]
            if value > remain:
                break
            path.append(value)
            _dfs(candidate_index, remain - value, path)
            path.pop()

    _dfs(0, target, [])
    return output

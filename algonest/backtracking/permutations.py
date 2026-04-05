"""Backtracking permutation generators."""

from typing import Iterable, List, Sequence


def all_permutations(values: Sequence[int]) -> List[List[int]]:
    """Return all permutations (may include duplicates)."""
    nums = list(values)
    output: List[List[int]] = []

    def _dfs(index: int) -> None:
        if index == len(nums):
            output.append(nums[:])
            return
        for swap_index in range(index, len(nums)):
            nums[index], nums[swap_index] = nums[swap_index], nums[index]
            _dfs(index + 1)
            nums[index], nums[swap_index] = nums[swap_index], nums[index]

    _dfs(0)
    return output


def permutations_no_duplicates(values: Iterable[int]) -> List[List[int]]:
    """Return unique permutations."""
    nums = sorted(list(values))
    used = [False] * len(nums)
    output: List[List[int]] = []

    def _dfs(path: List[int]) -> None:
        if len(path) == len(nums):
            output.append(path[:])
            return
        for candidate_index in range(len(nums)):
            if used[candidate_index]:
                continue
            if (
                candidate_index > 0
                and nums[candidate_index] == nums[candidate_index - 1]
                and not used[candidate_index - 1]
            ):
                continue
            used[candidate_index] = True
            path.append(nums[candidate_index])
            _dfs(path)
            path.pop()
            used[candidate_index] = False

    _dfs([])
    return output

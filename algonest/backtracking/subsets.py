"""Backtracking subset generators."""

from typing import Iterable, List, Sequence


def all_subsets(values: Sequence[int]) -> List[List[int]]:
    """Return power set of values."""
    nums = list(values)
    output: List[List[int]] = [[]]
    for value in nums:
        output.extend([subset + [value] for subset in output])
    return output


def subsets_no_duplicates(values: Iterable[int]) -> List[List[int]]:
    """Return unique subsets for multiset input."""
    nums = sorted(list(values))
    output: List[List[int]] = [[]]
    start = 0

    for value_index, value in enumerate(nums):
        if value_index > 0 and nums[value_index] == nums[value_index - 1]:
            current_start = start
        else:
            current_start = 0
        start = len(output)
        for output_index in range(current_start, len(output)):
            output.append(output[output_index] + [value])

    return output

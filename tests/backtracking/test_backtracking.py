"""Tests for backtracking utility package."""

from algonest.backtracking import (
    all_permutations,
    all_subsets,
    combination_sum,
    combinations,
    permutations_no_duplicates,
    subsets_no_duplicates,
)


def test_permutations_helpers() -> None:
    assert sorted(all_permutations([1, 2])) == [[1, 2], [2, 1]]
    assert sorted(permutations_no_duplicates([1, 1, 2])) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]


def test_combination_helpers() -> None:
    assert combinations([1, 2, 3], 2) == [[1, 2], [1, 3], [2, 3]]
    assert [2, 2, 3] in combination_sum([2, 3, 6, 7], 7)


def test_subset_helpers() -> None:
    assert sorted(all_subsets([1, 2])) == [[], [1], [1, 2], [2]]
    assert sorted(subsets_no_duplicates([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

"""Tests for permutation helpers."""

from algonest import next_permutation, prev_permutation


def test_next_permutation_happy_path() -> None:
    assert next_permutation([1, 2, 3]) == [1, 3, 2]


def test_next_permutation_wraps_to_smallest() -> None:
    assert next_permutation([3, 2, 1]) == [1, 2, 3]


def test_prev_permutation_happy_path() -> None:
    assert prev_permutation([1, 3, 2]) == [1, 2, 3]


def test_prev_permutation_wraps_to_largest() -> None:
    assert prev_permutation([1, 2, 3]) == [3, 2, 1]

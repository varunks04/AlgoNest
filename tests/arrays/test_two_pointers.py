"""Tests for two-pointer array algorithms."""

import pytest

from algonest import container_with_water, remove_duplicates, two_sum_sorted


def test_two_sum_sorted_happy_path() -> None:
    assert two_sum_sorted([1, 2, 4, 7, 11], 9) == (1, 3)


def test_two_sum_sorted_returns_negative_pair_when_missing() -> None:
    assert two_sum_sorted([1, 2, 4, 7, 11], 20) == (-1, -1)


def test_remove_duplicates_returns_unique_count() -> None:
    assert remove_duplicates([1, 1, 2, 2, 3]) == 3


def test_container_with_water_happy_path() -> None:
    assert container_with_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_container_with_water_raises_for_negative_height() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        container_with_water([1, -1, 2])

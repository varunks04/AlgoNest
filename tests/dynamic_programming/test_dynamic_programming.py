"""Consolidated tests for dynamic-programming utilities."""

import pytest

from algonest.dynamic_programming import (
    coin_change_ways,
    edit_distance,
    fib_memo,
    fib_space_optimized,
    fib_tabulated,
    knapsack_01,
    lcs_length,
    lis_length,
    matrix_chain_order,
    min_coins,
    min_path_sum,
    partition_equal_subset,
    subset_sum,
    unbounded_knapsack,
    unique_paths,
)


def test_min_coins_happy_path() -> None:
    assert min_coins([1, 2, 5], 11) == 3


def test_coin_change_ways_happy_path() -> None:
    assert coin_change_ways([1, 2, 5], 5) == 4


def test_coin_change_helpers_raise_on_invalid_inputs() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        min_coins([1, 2], -1)
    with pytest.raises(ValueError, match="positive"):
        coin_change_ways([1, 0, 2], 5)


def test_edit_distance_happy_path() -> None:
    assert edit_distance("kitten", "sitting") == 3


def test_knapsack_variants_happy_path() -> None:
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    assert knapsack_01(weights, values, 7) == 9
    assert unbounded_knapsack(weights, values, 7) == 9


def test_knapsack_variants_raise_on_invalid_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        knapsack_01([1], [1, 2], 1)
    with pytest.raises(ValueError, match="non-negative"):
        unbounded_knapsack([1, 2], [1, 2], -1)


def test_lcs_length_happy_path() -> None:
    assert lcs_length("abcde", "ace") == 3


def test_lis_length_happy_path() -> None:
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_matrix_chain_order_happy_path() -> None:
    assert matrix_chain_order([1, 2, 3, 4]) == 18


def test_matrix_chain_order_raises_on_invalid_dims() -> None:
    with pytest.raises(ValueError, match="at least two"):
        matrix_chain_order([1])
    with pytest.raises(ValueError, match="positive"):
        matrix_chain_order([1, 0, 3])


def test_fibonacci_variants_match() -> None:
    assert fib_memo(10) == 55
    assert fib_tabulated(10) == 55
    assert fib_space_optimized(10) == 55


def test_fibonacci_variants_raise_on_negative_input() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fib_memo(-1)
    with pytest.raises(ValueError, match="non-negative"):
        fib_tabulated(-1)
    with pytest.raises(ValueError, match="non-negative"):
        fib_space_optimized(-1)


def test_unique_paths_happy_path() -> None:
    assert unique_paths(3, 2) == 3


def test_unique_paths_raises_on_non_positive_dimensions() -> None:
    with pytest.raises(ValueError, match="positive"):
        unique_paths(0, 2)


def test_min_path_sum_happy_path() -> None:
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7


def test_min_path_sum_raises_on_empty_grid() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        min_path_sum([])


def test_subset_sum_happy_path() -> None:
    assert subset_sum([3, 34, 4, 12, 5, 2], 9) is True


def test_partition_equal_subset_happy_path() -> None:
    assert partition_equal_subset([1, 5, 11, 5]) is True


def test_subset_helpers_raise_on_negative_values() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        subset_sum([1, -1, 2], 2)
    with pytest.raises(ValueError, match="non-negative"):
        partition_equal_subset([1, -1, 2])

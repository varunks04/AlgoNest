"""Tests for grouped binary-search-family functions."""

import pytest

from algonest import (
    binary_search,
    jump_search,
    linear_search,
    lower_bound,
    ternary_search,
    upper_bound,
)


def test_binary_search_finds_existing_target() -> None:
    assert binary_search([1, 3, 5, 7], 5) == 2


def test_binary_search_returns_minus_one_for_absent_target() -> None:
    assert binary_search([1, 3, 5, 7], 6) == -1


def test_lower_bound_returns_first_ge_index() -> None:
    assert lower_bound([1, 2, 2, 4], 2) == 1


def test_upper_bound_returns_first_greater_index() -> None:
    assert upper_bound([1, 2, 2, 4], 2) == 3


def test_binary_search_functions_support_tuple_and_numpy() -> None:
    assert lower_bound((1, 2, 2, 4), 2) == 1
    np = pytest.importorskip("numpy")
    assert upper_bound(np.array([1, 2, 2, 4]), 2) == 3


def test_binary_search_functions_raise_type_error_for_invalid_input() -> None:
    with pytest.raises(TypeError, match="Input must not be None"):
        binary_search(None, 1)


def test_linear_search_finds_target() -> None:
    assert linear_search([4, 2, 7], 7) == 2


def test_ternary_search_finds_target() -> None:
    assert ternary_search([1, 3, 5, 7, 9], 7) == 3


def test_jump_search_finds_target() -> None:
    assert jump_search([1, 3, 5, 7, 9], 5) == 2

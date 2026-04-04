import pytest

from algonest.utils import assert_sorted, time_function


def test_time_function_and_assert_sorted() -> None:
    value, elapsed = time_function(sum, [1, 2, 3])
    assert value == 6
    assert elapsed >= 0.0
    assert_sorted([1, 2, 3])
    with pytest.raises(ValueError, match="sorted"):
        assert_sorted([3, 2, 1])

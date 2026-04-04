import pytest

from algonest.utils import validate_iterable


def test_validate_iterable() -> None:
    assert validate_iterable((1, 2, 3)) == [1, 2, 3]
    with pytest.raises(TypeError, match="Input must not be None"):
        validate_iterable(None)
    with pytest.raises(TypeError, match="Input must be iterable"):
        validate_iterable(10)

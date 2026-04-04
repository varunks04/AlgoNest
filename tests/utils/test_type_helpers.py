from algonest.utils import ComparableT, NumberT


def test_type_helper_symbols_exist() -> None:
    assert NumberT is not None
    assert ComparableT is not None

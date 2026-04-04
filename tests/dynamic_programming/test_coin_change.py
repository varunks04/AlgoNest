from algonest.dynamic_programming import coin_change_ways, min_coins


def test_coin_change() -> None:
    assert min_coins([1, 2, 5], 11) == 3
    assert coin_change_ways([1, 2, 5], 5) == 4

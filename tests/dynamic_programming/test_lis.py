from algonest.dynamic_programming import lis_length


def test_lis() -> None:
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4

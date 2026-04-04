from algonest.dynamic_programming import matrix_chain_order


def test_matrix_chain() -> None:
    assert matrix_chain_order([1, 2, 3, 4]) == 18

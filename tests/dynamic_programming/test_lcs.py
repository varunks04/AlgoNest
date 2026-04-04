from algonest.dynamic_programming import lcs_length


def test_lcs() -> None:
    assert lcs_length("abcde", "ace") == 3

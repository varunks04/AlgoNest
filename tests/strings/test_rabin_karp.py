from algonest.strings import rabin_karp_search


def test_rabin_karp_search() -> None:
    assert rabin_karp_search("aaaaa", "aa") == [0, 1, 2, 3]

from algonest.strings import kmp_search


def test_kmp_search() -> None:
    assert kmp_search("ababcabcabababd", "ababd") == [10]

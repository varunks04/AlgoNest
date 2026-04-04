from algonest.strings import find_all_anagrams, group_anagrams, is_anagram


def test_anagram_utilities() -> None:
    assert is_anagram("listen", "silent") is True
    grouped = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert any(sorted(group) == ["ate", "eat", "tea"] for group in grouped)
    assert find_all_anagrams("cbaebabacd", "abc") == [0, 6]

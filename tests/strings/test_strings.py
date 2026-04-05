"""Consolidated tests for string utilities."""

import pytest

from algonest.strings import (
    Trie,
    find_all_anagrams,
    group_anagrams,
    is_anagram,
    is_palindrome,
    kmp_search,
    longest_palindromic_substring,
    rabin_karp_search,
    rolling_hash,
    z_array,
    z_search,
)


def test_anagram_helpers_happy_path() -> None:
    assert is_anagram("listen", "silent") is True
    grouped = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert any(sorted(group) == ["ate", "eat", "tea"] for group in grouped)
    assert find_all_anagrams("cbaebabacd", "abc") == [0, 6]


def test_kmp_search_happy_path() -> None:
    assert kmp_search("ababcabcabababd", "ababd") == [10]


def test_rabin_karp_search_happy_path() -> None:
    assert rabin_karp_search("aaaaa", "aa") == [0, 1, 2, 3]


def test_z_algorithm_helpers_happy_path() -> None:
    assert z_array("aaaa")[1] == 3
    assert z_search("aabcaabxaaaz", "aab") == [0, 4]


def test_trie_operations_happy_path() -> None:
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.starts_with("app") is True
    trie.delete("apple")
    assert trie.search("apple") is False


def test_palindrome_helpers_happy_path() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert longest_palindromic_substring("babad") in {"bab", "aba"}


def test_rolling_hash_stability_happy_path() -> None:
    assert rolling_hash("algo") == rolling_hash("algo")
    assert rolling_hash("algo") != rolling_hash("nest")


def test_rolling_hash_raises_on_invalid_parameters() -> None:
    with pytest.raises(ValueError, match="positive"):
        rolling_hash("algo", base=0)
    with pytest.raises(ValueError, match="positive"):
        rolling_hash("algo", mod=0)

from algonest.strings import Trie


def test_trie_ops() -> None:
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.starts_with("app") is True
    trie.delete("apple")
    assert trie.search("apple") is False

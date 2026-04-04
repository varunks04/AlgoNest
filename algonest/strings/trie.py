"""Trie implementation for prefix matching."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class _TrieNode:
    children: Dict[str, "_TrieNode"] = field(default_factory=dict)
    is_end: bool = False


class Trie:
    """Implement insert/search/prefix/delete operations in trie."""

    def __init__(self) -> None:
        self.root = _TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, word: str) -> bool:
        def _delete(node: _TrieNode, index: int) -> bool:
            if index == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            ch = word[index]
            if ch not in node.children:
                return False

            should_remove = _delete(node.children[ch], index + 1)
            if should_remove:
                del node.children[ch]
                return len(node.children) == 0 and not node.is_end
            return False

        return _delete(self.root, 0)

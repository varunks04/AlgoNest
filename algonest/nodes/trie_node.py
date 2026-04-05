"""Canonical trie node definition."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class TrieNode:
    """Node for trie/prefix tree structures."""

    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_end: bool = False

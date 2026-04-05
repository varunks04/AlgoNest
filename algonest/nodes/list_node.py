"""Canonical linked-list node definition."""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ListNode:
    """Node for singly linked-list style structures."""

    value: Any
    next: Optional["ListNode"] = None

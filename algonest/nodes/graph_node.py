"""Canonical graph node definition."""

from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class GraphNode:
    """Node for adjacency-list style graph problems."""

    value: Any
    neighbors: List["GraphNode"] = field(default_factory=list)

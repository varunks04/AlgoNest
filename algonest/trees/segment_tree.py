"""Segment tree supporting sum/min/max queries and point updates."""

from typing import List


class SegmentTree:
    """Implement segment tree for range queries."""

    def __init__(self, values: List[int]) -> None:
        if not isinstance(values, list):
            raise TypeError("values must be a list")
        if not values:
            raise ValueError("values cannot be empty")
        self.n = len(values)
        self.sum_tree = [0] * (4 * self.n)
        self.min_tree = [0] * (4 * self.n)
        self.max_tree = [0] * (4 * self.n)
        self._build(values, 1, 0, self.n - 1)

    def _build(self, values: List[int], idx: int, left: int, right: int) -> None:
        if left == right:
            self.sum_tree[idx] = values[left]
            self.min_tree[idx] = values[left]
            self.max_tree[idx] = values[left]
            return
        mid = (left + right) // 2
        self._build(values, idx * 2, left, mid)
        self._build(values, idx * 2 + 1, mid + 1, right)
        self._pull(idx)

    def _pull(self, idx: int) -> None:
        self.sum_tree[idx] = self.sum_tree[idx * 2] + self.sum_tree[idx * 2 + 1]
        self.min_tree[idx] = min(self.min_tree[idx * 2], self.min_tree[idx * 2 + 1])
        self.max_tree[idx] = max(self.max_tree[idx * 2], self.max_tree[idx * 2 + 1])

    def point_update(self, pos: int, value: int) -> None:
        """Update one position with new value."""
        if pos < 0 or pos >= self.n:
            raise IndexError("pos out of range")
        self._update(1, 0, self.n - 1, pos, value)

    def _update(self, idx: int, left: int, right: int, pos: int, value: int) -> None:
        if left == right:
            self.sum_tree[idx] = value
            self.min_tree[idx] = value
            self.max_tree[idx] = value
            return
        mid = (left + right) // 2
        if pos <= mid:
            self._update(idx * 2, left, mid, pos, value)
        else:
            self._update(idx * 2 + 1, mid + 1, right, pos, value)
        self._pull(idx)

    def range_sum(self, ql: int, qr: int) -> int:
        """Return sum in inclusive range [ql, qr]."""
        return self._query_sum(1, 0, self.n - 1, ql, qr)

    def _query_sum(self, idx: int, left: int, right: int, ql: int, qr: int) -> int:
        if ql <= left and right <= qr:
            return self.sum_tree[idx]
        if right < ql or qr < left:
            return 0
        mid = (left + right) // 2
        return self._query_sum(idx * 2, left, mid, ql, qr) + self._query_sum(
            idx * 2 + 1,
            mid + 1,
            right,
            ql,
            qr,
        )

    def range_min(self, ql: int, qr: int) -> int:
        """Return minimum in inclusive range [ql, qr]."""
        return self._query_min(1, 0, self.n - 1, ql, qr)

    def _query_min(self, idx: int, left: int, right: int, ql: int, qr: int) -> int:
        if ql <= left and right <= qr:
            return self.min_tree[idx]
        if right < ql or qr < left:
            return 10**18
        mid = (left + right) // 2
        return min(
            self._query_min(idx * 2, left, mid, ql, qr),
            self._query_min(idx * 2 + 1, mid + 1, right, ql, qr),
        )

    def range_max(self, ql: int, qr: int) -> int:
        """Return maximum in inclusive range [ql, qr]."""
        return self._query_max(1, 0, self.n - 1, ql, qr)

    def _query_max(self, idx: int, left: int, right: int, ql: int, qr: int) -> int:
        if ql <= left and right <= qr:
            return self.max_tree[idx]
        if right < ql or qr < left:
            return -(10**18)
        mid = (left + right) // 2
        return max(
            self._query_max(idx * 2, left, mid, ql, qr),
            self._query_max(idx * 2 + 1, mid + 1, right, ql, qr),
        )

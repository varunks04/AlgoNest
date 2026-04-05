"""Interval-based array utility functions."""

from typing import Iterable, List, Sequence, Tuple

from algonest.utils import _validate_iterable

Interval = Tuple[int, int]


def _normalize_intervals(intervals: Iterable[Sequence[int]]) -> List[Interval]:
    raw = _validate_iterable(intervals)
    normalized: List[Interval] = []
    for interval in raw:
        pair = _validate_iterable(interval)
        if len(pair) != 2:
            raise ValueError("Each interval must contain exactly two values")
        start, end = pair
        if start > end:
            raise ValueError("Interval start must be <= end")
        normalized.append((start, end))
    return normalized


def merge_intervals(intervals: Iterable[Sequence[int]]) -> List[Interval]:
    """Merge overlapping intervals and return sorted non-overlapping intervals."""
    pairs = _normalize_intervals(intervals)
    if not pairs:
        return []

    pairs.sort(key=lambda x: x[0])
    merged: List[Interval] = [pairs[0]]

    for start, end in pairs[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def insert_interval(
    intervals: Iterable[Sequence[int]], new_interval: Sequence[int]
) -> List[Interval]:
    """Insert and merge one interval into an interval list."""
    pairs = _normalize_intervals(intervals)
    addition = _normalize_intervals([new_interval])[0]
    return merge_intervals(pairs + [addition])


def non_overlapping_count(intervals: Iterable[Sequence[int]]) -> int:
    """Return minimum intervals to remove to make intervals non-overlapping."""
    pairs = _normalize_intervals(intervals)
    if not pairs:
        return 0

    pairs.sort(key=lambda x: x[1])
    keep = 1
    current_end = pairs[0][1]

    for start, end in pairs[1:]:
        if start >= current_end:
            keep += 1
            current_end = end

    return len(pairs) - keep

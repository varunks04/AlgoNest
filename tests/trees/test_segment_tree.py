from algonest.trees import SegmentTree


def test_segment_tree_ops() -> None:
    segment = SegmentTree([1, 3, 5, 7, 9, 11])
    assert segment.range_sum(1, 3) == 15
    assert segment.range_min(1, 4) == 3
    assert segment.range_max(1, 4) == 9
    segment.point_update(2, 6)
    assert segment.range_sum(1, 3) == 16

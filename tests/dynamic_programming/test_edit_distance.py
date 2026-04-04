from algonest.dynamic_programming import edit_distance


def test_edit_distance() -> None:
    assert edit_distance("kitten", "sitting") == 3

from algonest.utils import read_ints_from_text, write_lines


def test_fast_io_helpers() -> None:
    assert read_ints_from_text("1 2 3\n4") == [1, 2, 3, 4]
    assert write_lines(["a", "b"]) == "a\nb\n"

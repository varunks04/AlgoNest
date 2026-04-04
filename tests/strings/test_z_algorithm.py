from algonest.strings import z_array, z_search


def test_z_algorithm_functions() -> None:
    assert z_array("aaaa")[1] == 3
    assert z_search("aabcaabxaaaz", "aab") == [0, 4]

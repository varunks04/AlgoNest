from algonest.utils import build_pytest_command


def test_build_pytest_command() -> None:
    assert build_pytest_command("tests") == [
        "python",
        "-m",
        "pytest",
        "-q",
        "tests",
    ]

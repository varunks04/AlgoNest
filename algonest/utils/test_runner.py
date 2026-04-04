"""Helpers to run local test suites consistently."""

import subprocess
from typing import List, Optional


DEFAULT_TEST_PATH = "tests"


def build_pytest_command(test_path: str = DEFAULT_TEST_PATH) -> List[str]:
    """Build canonical pytest command tokens.

    Args:
        test_path (str): Target test path.

    Returns:
        List[str]: Command tokens suitable for subprocess execution.

    Raises:
        TypeError: If test_path is not a string.

    Time Complexity: O(1)
    Space Complexity: O(1)

    Example:
        >>> build_pytest_command("tests")
        ['python', '-m', 'pytest', '-q', 'tests']
    """
    if not isinstance(test_path, str):
        raise TypeError("test_path must be a string")
    return ["python", "-m", "pytest", "-q", test_path]


def run_tests(test_path: str = DEFAULT_TEST_PATH) -> int:
    """Run pytest for the given path and return process exit code.

    Args:
        test_path (str): Target path for pytest.

    Returns:
        int: Process return code (0 indicates success).

    Raises:
        TypeError: If test_path is not a string.

    Time Complexity: O(t)
    Space Complexity: O(1)

    Example:
        >>> isinstance(run_tests, object)
        True
    """
    command = build_pytest_command(test_path)
    completed: Optional[subprocess.CompletedProcess[str]] = subprocess.run(
        command,
        capture_output=False,
        text=True,
    )
    return completed.returncode

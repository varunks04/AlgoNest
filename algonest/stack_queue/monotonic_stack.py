"""Monotonic stack algorithms."""

from typing import List


def next_greater_element(nums: List[int]) -> List[int]:
    """Return next greater element for each position.

    Args:
        nums (List[int]): Input integer list.

    Returns:
        List[int]: Next greater values or -1 where absent.

    Raises:
        TypeError: If nums is not a list of integers.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> next_greater_element([2, 1, 2, 4, 3])
        [4, 2, 4, -1, -1]
    """
    if not isinstance(nums, list):
        raise TypeError("nums must be a list")
    for value in nums:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("nums must contain integers")

    result = [-1] * len(nums)
    stack: List[int] = []

    for index, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            result[stack.pop()] = value
        stack.append(index)

    return result


def largest_rectangle_in_histogram(heights: List[int]) -> int:
    """Return largest rectangle area from histogram heights.

    Args:
        heights (List[int]): Non-negative bar heights.

    Returns:
        int: Maximum rectangle area.

    Raises:
        TypeError: If input is not list of integers.
        ValueError: If any height is negative.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3])
        10
    """
    if not isinstance(heights, list):
        raise TypeError("heights must be a list")
    for value in heights:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("heights must contain integers")
        if value < 0:
            raise ValueError("heights must be non-negative")

    max_area = 0
    stack: List[int] = []
    values = heights + [0]

    for index, height in enumerate(values):
        while stack and values[stack[-1]] > height:
            top = stack.pop()
            left = stack[-1] if stack else -1
            width = index - left - 1
            area = values[top] * width
            if area > max_area:
                max_area = area
        stack.append(index)

    return max_area

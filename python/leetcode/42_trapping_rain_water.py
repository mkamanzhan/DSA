# Hard

# Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack

# Link: https://leetcode.com/problems/trapping-rain-water

# Given n non-negative integers representing an elevation map where 
# the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive Dynamic Programming Approach
# Time: O(n)
# Space: O(n)
def solution_1(height: list[int]) -> int:
    D_left = [0] * len(height)
    D_left[0] = height[0]

    D_right = [0] * len(height)
    D_right[-1] = height[-1]

    for i in range(1, len(height)):
        D_left[i] = max(D_left[i - 1], height[i])

    for i in range(len(height) - 2, -1, -1):
        D_right[i] = max(D_right[i + 1], height[i])
    
    result = 0
    for i in range(len(height)):
        result += min(D_left[i], D_right[i]) - height[i]
    
    return result


# Two Pointer Approach
# Time: O(n)
# Space: O(1)
def solution_2(height: list[int]) -> int:
    left_max = height[0]
    right_max = height[-1]

    if len(height) <= 2:
        return 0
    
    left = 1
    right = len(height) - 2

    result = 0
    while left <= right:
        if left_max < right_max:
            left_max = max(left_max, height[left])
            result += max(0, min(left_max, right_max) - height[left])
            left += 1
        else:
            right_max = max(right_max, height[right])
            result += max(0, min(left_max, right_max) - height[right])
            right -= 1

    return result


class _Data(NamedTuple):
    height: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            height=[0,1,0,2,1,0,1,3,2,1,2,1],
        ),
        expected=6,
    ),
    TestCase(
        params=_Data(
            height=[4,2,0,3,2,5],
        ),
        expected=9,
    ),
    TestCase(
        params=_Data(
            height=[4,2,3],
        ),
        expected=1,
    ),
]


profile_solutions(
    [
        solution_1, 
        solution_2
    ], 
    test_cases,
)

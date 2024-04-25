# Medium

# Topics: Array, Dynamic Programming, Greedy 

# Link: https://leetcode.com/problems/jump-game

# You are given an integer array nums. You are initially positioned at the 
# array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive Dynamic Programming 
# Time: O(n^2)
# Space: O(n)
def solution_1(nums: list[int]) -> bool:
    m = [False] * len(nums)
    m[0] = True

    for i in range(len(nums)):
        if m[i] is False:
            continue
        for j in range(1, nums[i] + 1):
            if i + j >= len(nums):
                break
            m[i + j] = True
        if m[-1]:
            return True
    return False


# Greedy
# Time: O(n)
# Space: O(1)
def solution_2(nums: list[int]) -> bool:
    turns_left = 0
    for n in nums:
        if turns_left < 0:
            return False
        turns_left = max(n, turns_left)
        turns_left -= 1
    return True


class _Data(NamedTuple):
    nums: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums=[2,3,1,1,4],
        ),
        expected=True,
    ),
    TestCase(
        params=_Data(
            nums=[3,2,1,0,4],
        ),
        expected=False,
    ),
    TestCase(
        params=_Data(
            nums=[1,2],
        ),
        expected=True,
    ),
    TestCase(
        params=_Data(
            nums=[0,2,3],
        ),
        expected=False,
    ),
    TestCase(
        params=_Data(
            nums=[3, 2, 1, 0],
        ),
        expected=True,
    ),
    TestCase(
        params=_Data(
            nums=[0],
        ),
        expected=True,
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2,
    ], 
    test_cases,
)

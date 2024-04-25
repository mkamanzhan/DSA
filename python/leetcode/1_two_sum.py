# Easy

# Topics: String, Two Pointers 

# Link: https://leetcode.com/problems/two-sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Two Pointer
# Time: O(n * lon(n))
# Space: O(n)
def solution_1(nums: list[int], target: int) -> list[int]:
    arr = sorted(
        [(n, i) for i, n in enumerate(nums)],
        key=lambda x: x[0],
    )

    l = 0
    r = len(arr) - 1

    while l < r:
        _sum = arr[l][0] + arr[r][0]
        if _sum == target:
            return [arr[l][1], arr[r][1]]
        if _sum < target:
            l += 1
        else:
            r -= 1

    raise NotImplemented


# Dynamic Programming
# Time: O(n)
# Space: O(n)
def solution_2(nums: list[int], target: int) -> list[int]:
    D = {}

    for i, n in enumerate(nums):
        D_val = D.get(target - n)
        if D_val is not None:
            return [D_val, i]
        D[n] = i
    raise NotImplemented


class _Data(NamedTuple):
    nums: list[int]
    target: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums=[2,7,11,15],
            target=9,
        ),
        expected=[0,1],
    ),
    TestCase(
        params=_Data(
            nums=[3,2,4],
            target=6,
        ),
        expected=[1,2],
    ),
    TestCase(
        params=_Data(
            nums=[3,3],
            target=6,
        ),
        expected=[0,1],
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2,
    ], 
    test_cases,
)

# Medium

# Topics: Array, Divide and Conquer, Dynamic Programming, Greedy 

# Link: https://leetcode.com/problems/maximum-subarray

# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive Dynamic Programming 
# Time: O(n^2)
# Space: O(n^2)
def solution_1(nums: list[int]) -> int:
    D = [[0] * len(nums)] * len(nums)

    max_sum = -10^5

    for i in range(len(nums)):
        for j in range(i + 1):
            if i == j:
                D[i][j] = nums[i]
            else:
                D[i][j] = D[i - 1][j] + nums[i]
            if D[i][j] > max_sum:
                max_sum = D[i][j]

    return max_sum


# Naive Greedy 
# Time: O(n)
# Space: O(1)
def solution_2(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    partition_sum = nums[0]
    max_sum = partition_sum

    for n in nums[1:]:
        partition_sum = max(n, n + partition_sum)
        if partition_sum > max_sum:
            max_sum = partition_sum
    return max_sum


class _Data(NamedTuple):
    nums: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums=[-2,1,-3,4,-1,2,1,-5,4],
        ),
        expected=6,
    ),
    TestCase(
        params=_Data(
            nums=[1],
        ),
        expected=1,
    ),
    TestCase(
        params=_Data(
            nums=[5,4,-1,7,8],
        ),
        expected=23,
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2,
    ], 
    test_cases,
)

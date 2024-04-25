# Hard

# Topics: Array, Hash Map

# Link: https://leetcode.com/problems/first-missing-positive

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Hast Map
# Time: O(n)
# Space: O(1)
def solution_1(
    nums: list[int],
) -> int:
    i = 0
    while i < len(nums):
        n = nums[i]
        new_pos = n - 1
        if new_pos < 0 or new_pos >= len(nums) or nums[new_pos] == n:
            i += 1
            continue
        nums[new_pos], nums[i] = nums[i], nums[new_pos]

    for i, n in enumerate(nums):
        if i != n - 1:
            return i + 1
    return len(nums) + 1


class _Data(NamedTuple):
    nums: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums=[1,2,0],
        ),
        expected=3,
    ),
    TestCase(
        params=_Data(
            nums=[3,4,-1,1],
        ),
        expected=2,
    ),
    TestCase(
        params=_Data(
            nums=[7,8,9,11,12],
        ),
        expected=1,
    ),
    TestCase(
        params=_Data(
            nums=[1, 1],
        ),
        expected=2,
    ),
]


profile_solutions(
    [
        solution_1,
    ], 
    test_cases,
)

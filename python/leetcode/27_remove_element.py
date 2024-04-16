# Easy

# Topics: Array, Two Pointers

# Link: https://leetcode.com/problems/remove-element/

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.


# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import NamedTuple

from infra.asserts import assert_solutions, profile_solutions, TestCase


def solution_1(nums: list[int], val: int) -> int:
    i = 0
    j = len(nums) - 1

    if len(nums) == 0:
        return 0

    while i < j:
        if nums[i] != val:
            i = i + 1
        elif nums[i] == nums[j] == val:
            j = j - 1
        elif nums[i] == val and nums[j] != val:
            nums[i], nums[j] = nums[j], nums[i]
            j = j - 1
            i = i + 1

    if nums[i] != val:
        i = i + 1            
    
    return i


def solution_2(nums: list[int], val: int) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j = j + 1
    return j


class _Data(NamedTuple):
    nums: list[int]
    val: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(nums=[5, 5, 5, 5, 5], val=5),
        expected=0,
    ),
    TestCase(
        params=_Data(nums=[5, 5, 5, 5, 5], val=3),
        expected=5,
    ),
    TestCase(
        params=_Data(nums=[3,2,2,3], val=3),
        expected=2,
    ),
    TestCase(
        params=_Data(nums=[0,1,2,2,3,0,4,2], val=2),
        expected=5,
    ),
    TestCase(
        params=_Data(nums=[1], val=1),
        expected=0,
    ),
    TestCase(
        params=_Data(nums=[], val=1),
        expected=0,
    ),
    TestCase(
        params=_Data(nums=[2] * 100, val=1),
        expected=100,
    ),
    TestCase(
        params=_Data(nums=[2] * 100, val=2),
        expected=0,
    )
]

assert_solutions([solution_1, solution_2], test_cases)
profile_solutions([solution_1, solution_2], test_cases)

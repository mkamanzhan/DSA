# Medium

# Topics: Array, Two Pointers

# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place 
# such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, then 
# the first k elements of nums should hold the final result. It does not matter 
# what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


def solution_1(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    j = 2
    for i in range(2, len(nums)):
        if not (nums[j - 2] == nums[i]):
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return j


class _Data(NamedTuple):
    nums: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums=[1,1,1,2,2,3],
        ),
        expected=5,
    ),
    TestCase(
        params=_Data(
            nums=[0,0,1,1,1,1,2,3,3],
        ),
        expected=7,
    ),
    TestCase(
        params=_Data(
            nums=[0],
        ),
        expected=1,
    ),
    TestCase(
        params=_Data(
            nums=[0, 1],
        ),
        expected=2,
    ),
    TestCase(
        params=_Data(
            nums=[0, 1, 1, 1],
        ),
        expected=3,
    ),
]


profile_solutions(solution_1, test_cases)

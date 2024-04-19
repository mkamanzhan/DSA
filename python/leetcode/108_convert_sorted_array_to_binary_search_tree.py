# Easy

# Topics: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

# Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.


# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

from typing import NamedTuple

from data_structures import TreeNode
from infra.asserts import profile_solutions, TestCase
import math


def solution_1(nums: list[int]) -> TreeNode | None:
    def rec(l: int, r: int) -> TreeNode | None:
        if l == r:
            return TreeNode(val=nums[l])
        if l > r:
            return None
        
        c = math.ceil(l + (r - l) / 2)

        node = TreeNode(
            val=nums[c],
            left=rec(l, c - 1),
            right=rec(c + 1, r),
        )
        return node
    
    return rec(0, len(nums) - 1)


def solution_2(nums: list[int]) -> TreeNode | None:
    def rec(left: int, right: int) -> TreeNode | None:
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(val=nums[mid])
        node.left = rec(left, mid - 1)
        node.right = rec(mid + 1, right)
        return node

    return rec(0, len(nums) - 1)


class _Data(NamedTuple):
    nums: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums=[-10,-3,0,5,9],
        ),
        expected=[0,-3,9,-10,None,5],
    ),
    TestCase(
        params=_Data(
            nums=[1,3],
        ),
        expected=[3,1],
    ),
]


profile_solutions([solution_1, solution_2], test_cases)

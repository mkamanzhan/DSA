# Easy

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
# Answers within 10-5 of the actual answer will be accepted.


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:

# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]

from typing import NamedTuple

from data_structures import TreeNode, list_to_tree_node
from infra.asserts import profile_solutions, TestCase


def solution_1(root: TreeNode | None) -> list[int]:
    result = []
    if root is None:
        return result
    
    to_unpack = [[root]]

    while to_unpack:
        unpacking = to_unpack.pop()
        next_to_unpack = []
        level_sum = 0
        level_count = 0
        for node in unpacking:
            level_sum += node.val
            level_count += 1

            if node.left:
                next_to_unpack.append(node.left)
            if node.right:
                next_to_unpack.append(node.right)

        if next_to_unpack:
            to_unpack.append(next_to_unpack)
        
        result.append(round(level_sum / level_count, 5))
    
    return result


class _Data(NamedTuple):
    root: TreeNode | None


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            root=list_to_tree_node([3,9,20,None,None,15,7]),
        ),
        expected=[3.00000,14.50000,11.00000],
    ),
    TestCase(
        params=_Data(
            root=list_to_tree_node([3,9,20,15,7]),
        ),
        expected=[3.00000,14.50000,11.00000],
    ),
]


profile_solutions(solution_1, test_cases)

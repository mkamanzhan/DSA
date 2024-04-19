# Easy

# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree

# Link: https://leetcode.com/problems/same-tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

from typing import NamedTuple

from data_structures import TreeNode, list_to_tree_node
from infra.asserts import profile_solutions, TestCase


def solution_1(p: TreeNode | None, q: TreeNode | None) -> bool:
    def rec(node_1: TreeNode | None, node_2: TreeNode | None) -> bool:
        if node_1 is None and node_2 is None:
            return True
    
        if node_1 is None or node_2 is None or node_1.val != node_2.val:
            return False
        
        return rec(node_1.left, node_2.left) and rec(node_1.right, node_2.right)

    return rec(p, q)


class _Data(NamedTuple):
    p: TreeNode | None
    q: TreeNode | None


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            p=list_to_tree_node([1,2,3]),
            q=list_to_tree_node([1,2,3]),
        ),
        expected=True,
    ),
    TestCase(
        params=_Data(
            p=list_to_tree_node([1,2]),
            q=list_to_tree_node([1,None,2]),
        ),
        expected=False,
    ),
    TestCase(
        params=_Data(
            p=list_to_tree_node([1,2,1]),
            q=list_to_tree_node([1,1,2]),
        ),
        expected=False,
    ),
]


profile_solutions(solution_1, test_cases)

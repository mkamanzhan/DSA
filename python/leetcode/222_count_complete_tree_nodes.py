# Easy

# Topics: Binary Search, Tree, Binary Tree

# Link: https://leetcode.com/problems/count-complete-tree-nodes

# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last,
# is completely filled in a complete binary tree, and all nodes in the last
# level are as far left as possible. It can have between 1 and 2h nodes
# inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.


# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase
from data_structures import TreeNode, list_to_tree_node


# Naive DFS
# Time: O(n)
# Space: O(1)
def solution_1(
    root: TreeNode | None,
) -> int:
    if root is None:
        return 0

    return 1 + solution_1(root.left) + solution_1(root.right)


# DFS
# Time: O(lon(n)^2)
# Space: O(1)
def solution_2(
    root: TreeNode | None,
) -> int:
    def rec(node: TreeNode | None) -> int:
        if node is None:
            return 0
        
        left_height = get_left_height(node)
        right_height = get_right_height(node)

        if left_height == right_height:
            return 2 ** left_height - 1
        
        return 1 + rec(node.left) + rec(node.right)
        
    def get_left_height(node: TreeNode | None) -> int:
        h = 0
        c = node
        while c:
            h += 1
            c = c.left
        return h
    
    def get_right_height(node: TreeNode| None) -> int:
        h = 0
        c = node
        while c:
            h += 1
            c = c.right
        return h

    return rec(root)


class _Data(NamedTuple):
    root: TreeNode | None


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            root=list_to_tree_node([1,2,3,4,5,6])
        ),
        expected=6,
    ),
    TestCase(
        params=_Data(
            root=list_to_tree_node([]),
        ),
        expected=0,
    ),
    TestCase(
        params=_Data(
            root=list_to_tree_node([1]),
        ),
        expected=1,
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2,
    ], 
    test_cases,
)

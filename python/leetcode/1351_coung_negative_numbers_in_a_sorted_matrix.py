# Easy

# Topics: Array, Binary Search


# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

# Given a m x n matrix grid which is sorted in non-increasing order
# both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Greedy Approach
# Time: O(m + n)
# Space: O(1)
def solution_1(
    grid: list[list[int]],
) -> int:
    i = len(grid) - 1
    j = 0
    c = 0

    while j < len(grid[0]) and i >= 0:
        if grid[i][j] < 0:
            c += len(grid[0]) - j
            i -= 1
        else:
            j += 1
    
    return c


class _Data(NamedTuple):
    grid: list[list[int]]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            grid=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
        ),
        expected=8,
    ),
    TestCase(
        params=_Data(
            grid=[[3,2],[1,0]],
        ),
        expected=0,
    ),
    TestCase(
        params=_Data(
            grid=[[4,3,2,-1],[3,0,-1,-2],[2,-1,-3,-5]],
        ),
        expected=6,
    ),
]


profile_solutions(
    [
        solution_1,
    ], 
    test_cases,
)

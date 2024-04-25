# Medium

# Topics: Array, String, Backtracking, Matrix

# Link: https://leetcode.com/problems/word-search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false


# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


# Follow up: Could you use search pruning to make your solution faster with a larger board?

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive DFS
# Time: O(m * n * 4^word)
# Space: O(m * n)
def solution_1(
    board: list[list[str]],
    word: str,
) -> bool:
    visited = [
        [False] * len(board[0])
        for _ in range(len(board))
    ]

    def traverse(
        i: int,
        j: int,
        k: int = 0,
    ) -> bool:
        if board[j][i] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        nonlocal visited
        visited[j][i] = True
        
        lookup = []
        if i > 0:
            lookup.append((i - 1, j))
        if j > 0:
            lookup.append((i, j - 1))
        if i < len(board[j]) - 1:
            lookup.append((i + 1, j))
        if j < len(board) - 1:
            lookup.append((i, j + 1))
        
        for q, p in lookup:
            if visited[p][q]:
                continue

            res = traverse(q, p, k + 1)
            if res is True:
                return True
        
        visited[j][i] = False
        return False

    for j in range(len(board)):
        for i in range(len(board[j])):
            res = traverse(i, j)
            if res is True:
                return True
    return False


class _Data(NamedTuple):
    board: list[list[str]]
    word: str


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            word="ABCCED",
        ),
        expected=True,
    ),
    TestCase(
        params=_Data(
            board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            word="SEE",
        ),
        expected=True,
    ),
    TestCase(
        params=_Data(
            board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            word="ABCB",
        ),
        expected=False,
    ),
    TestCase(
        params=_Data(
            board=[["C","A","A"],["A","A","A"],["B","C","D"]], 
            word="AAB",
        ),
        expected=True,
    ),
]


profile_solutions(
    [
        solution_1,
    ], 
    test_cases,
)

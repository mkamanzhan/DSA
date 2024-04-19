# Easy

# Topics: Math, Dynamic Programming, Memoization

# Link: https://leetcode.com/problems/climbing-stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Constraints:

# 1 <= n <= 45


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Time: O(n)
# Space: O(n)
def solution_1(n: int) -> int:
    D = [1, 2]
    for i in range(2, n + 1):
        D.append(D[i - 1] + D[i - 2])
    return D[n - 1]


# Time: O(n)
# Space: O(1)
def solution_2(n: int) -> int:
    if n in (1, 2, 3):
        return n

    first = 1
    second = 2
    last = 0
    for _ in range(3, n + 1):
        last = first + second
        first = second
        second = last

    return last

class _Data(NamedTuple):
    n: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            n=2,
        ),
        expected=2,
    ),
    TestCase(
        params=_Data(
            n=3,
        ),
        expected=3,
    ),
    TestCase(
        params=_Data(
            n=5,
        ),
        expected=8,
    ),
]


profile_solutions([solution_1, solution_2], test_cases)

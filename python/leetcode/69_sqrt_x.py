# Hard

# Topics: Math, Binary Search

# Link: https://leetcode.com/problems/sqrtx

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


# Constraints:

# 0 <= x <= 231 - 1

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Binary Search
# Time: O(log n)
# Space: O(1)
def solution_1(
    x: int,
) -> int:
    if x <= 1:
        return x
    
    left, right = 1, x + 1

    while left <= right:
        mid = (left + right) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            right = mid - 1
        else:
            left = mid + 1
    return right


# Newton's Method
# Time: O(log n)
# Space: O(1)
def solution_2(
    x: int,
) -> int:
    b = x
    while b * b > x:
        b = (b + x // b) // 2

    return b


class _Data(NamedTuple):
    x: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            x=4
        ),
        expected=2,
    ),
    TestCase(
        params=_Data(
            x=8,
        ),
        expected=2,
    ),
    TestCase(
        params=_Data(
            x=69,
        ),
        expected=8,
    ),
    TestCase(
        params=_Data(
            x=63,
        ),
        expected=7,
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2,
    ], 
    test_cases,
)

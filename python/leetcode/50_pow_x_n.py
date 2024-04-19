# Medium

# Topics: Math, Recursion

# Link: https://leetcode.com/problems/powx-n

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Time: O(log n)
# Space: O(log n)
def solution_1(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1

    if n < 0:
        x = 1/x
        n = abs(n)

    def rec(q: int) -> float:
        if q == 1:
            return x
        if q % 2 == 1:
            return x * rec(q - 1)
        else:
            r = rec(q // 2)
            return r * r

    return round(rec(n), 5)

# Time: O(log n)
# Space: O(1)
def solution_2(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    
    if n < 0:
        x = 1 / x
        n = -n

    a = 1
    while n > 0:
        if n % 2 == 0:
            x = x * x
            n = n // 2
        else:
            n = n - 1
            a = a * x
    return round(a, 5)


class _Data(NamedTuple):
    x: float
    n: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            x=2,
            n=10,
        ),
        expected=1024.00000,
    ),
    TestCase(
        params=_Data(
            x=2.1,
            n=3,
        ),
        expected=9.26100,
    ),
    TestCase(
        params=_Data(
            x=2,
            n=-2,
        ),
        expected=0.25,
    ),
    TestCase(
        params=_Data(
            x=0.00001,
            n=2147483647,
        ),
        expected=0.00000,
    ),
]


profile_solutions([solution_1, solution_2], test_cases)

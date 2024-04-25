# Easy

# Topics: Divide and Conquer, Bit Manipulation 

# Link: https://leetcode.com/problems/number-of-1-bits

# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits it has (also known as the Hamming weight).


# Example 1:

# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.


# Constraints:

# 1 <= n <= 231 - 1


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive Divide and Conquer 
# Time: O(log(n))
# Space: O(1)
def solution_1(n: int) -> int:
    count = 0
    while n > 0:
        count += n % 2
        n //= 2
    return count


# Bit Operators 
# Time: O(log(n))
# Space: O(1)
def solution_2(n: int) -> int:
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count


class _Data(NamedTuple):
    n: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            n=11,
        ),
        expected=3,
    ),
    TestCase(
        params=_Data(
            n=128,
        ),
        expected=1,
    ),
    TestCase(
        params=_Data(
            n=2147483645,
        ),
        expected=30,
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2,
    ], 
    test_cases,
)

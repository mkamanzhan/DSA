# Easy

# Topics: Two Pointers, String

# Link: https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative 
# positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


def solution_1(s: str, t: str) -> bool:
    j = 0

    if len(s) == 0:
        return True

    for c in t:
        if s[j] == c:
            j += 1
            if j == len(s):
                return True

    return False


class _Data(NamedTuple):
    s: str
    t: str


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(s="abc", t="ahbgdc"),
        expected=True,
    ),
    TestCase(
        params=_Data(s="axc", t="ahbgdc"),
        expected=False,
    ),
    TestCase(
        params=_Data(s="", t=""),
        expected=True,
    ),
    TestCase(
        params=_Data(s="a", t=""),
        expected=False,
    ),
    TestCase(
        params=_Data(s="", t="a"),
        expected=True,
    ),
    TestCase(
        params=_Data(s="a", t="b"),
        expected=False,
    ),
]


profile_solutions(solution_1, test_cases)

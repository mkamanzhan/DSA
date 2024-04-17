# Easy

# Topics: String, Hash Table

# Link: https://leetcode.com/problems/isomorphic-strings

# Given two strings s and t, determine if they are isomorphic

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# Example 2:

# Input: s = "foo", t = "bar"
# Output: false

# Example 3:

# Input: s = "paper", t = "title"
# Output: true

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


def solution_1(s: str, t: str) -> bool:
    m = {}
    occupied = set()

    for i in range(len(s)):
        if s[i] in m.keys():
            if m[s[i]] != t[i]:
                return False
        else:
            if t[i] in occupied:
                return False
    
            m[s[i]] = t[i]
            occupied.add(t[i])

    return True


class _Data(NamedTuple):
    s: str
    t: str


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(s="egg", t="add"),
        expected=True,
    ),
    TestCase(
        params=_Data(s="foo", t="bar"),
        expected=False,
    ),
    TestCase(
        params=_Data(s="paper", t="title"),
        expected=True,
    ),
    TestCase(
        params=_Data(s="a", t="b"),
        expected=True,
    ),
    TestCase(
        params=_Data(s="aaaa", t="basd"),
        expected=False,
    ),
    TestCase(
        params=_Data(s="badc", t="baba"),
        expected=False
    ),
]


profile_solutions(solution_1, test_cases)

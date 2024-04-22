# Easy

# Topics: Two Pointers, String, String Matching

# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

# Given two strings needle and haystack, return the index of the first occurrence 
# of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive Iterative
# Time: O(haystack * needle)
# Space: O(1)
def solution_1(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] != needle[0]:
            continue

        found = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                found = False
                break
        
        if found:
            return i
    
    return -1


class _Data(NamedTuple):
    haystack: str
    needle: str


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            haystack="sadbutsad",
            needle="sad",
        ),
        expected=0,
    ),
    TestCase(
        params=_Data(
            haystack="leetcode",
            needle="leeto",
        ),
        expected=-1,
    ),
    TestCase(
        params=_Data(
            haystack="leetcode",
            needle="code",
        ),
        expected=4,
    ),
]


profile_solutions(
    [
        solution_1,
    ], 
    test_cases,
)

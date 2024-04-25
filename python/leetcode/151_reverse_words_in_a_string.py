# Medium

# Topics: String, Two Pointers 

# Link: https://leetcode.com/problems/reverse-words-in-a-string

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. 
# Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.


# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# In Place Iterative
# Time: O(n^2)
# Space: O(1)
def solution_1(s: str) -> str:
    arr = list(s)
    arr = arr[::-1]

    def reverse_word(l: int, r: int) -> None:
        ln = r - l + 1
        for i in range(ln // 2):
            arr[l + i], arr[r - i] = arr[r-i], arr[l + i]
    
    def clear_whitespace() -> None:
        while arr[0] == " ":
            arr.pop(0)
        
        while arr[-1] == " ":
            arr.pop(-1)
        
        i = 0
        while i < (len(arr) - 1):
            if arr[i] == " " and arr[i + 1] == " ":
                arr.pop(i + 1)
            else:
                i += 1

    word_left_pos = None
    current_pos = 0
    while current_pos < len(arr):
        if arr[current_pos] != " " and word_left_pos is None:
            word_left_pos = current_pos
        elif arr[current_pos] == " " and word_left_pos is not None:
            reverse_word(word_left_pos, current_pos - 1)
            word_left_pos = None

        current_pos += 1
    if word_left_pos is not None:
        reverse_word(word_left_pos, len(arr) - 1)
    
    clear_whitespace()

    return "".join(arr)


class _Data(NamedTuple):
    s: str


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            s="the sky is blue",
        ),
        expected="blue is sky the",
    ),
    TestCase(
        params=_Data(
            s="  hello world  ",
        ),
        expected="world hello",
    ),
    TestCase(
        params=_Data(
            s="a good   example",
        ),
        expected="example good a",
    ),
    TestCase(
        params=_Data(
            s="EPY2giL",
        ),
        expected="EPY2giL",
    ),
]


profile_solutions(
    [
        solution_1,
    ], 
    test_cases,
)

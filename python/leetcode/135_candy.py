# Hard

# Topics: Array, Greedy

# Link: https://leetcode.com/problems/candy

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.


# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase


# Naive(Brute Force) Approach
# Time: O(n^2)
# Space: O(n)
def solution_1(ratings: list[int]) -> int:
    result = [0] * len(ratings)
    result[0] = 1

    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            result[i] = result[i - 1] + 1
        elif ratings[i - 1] == ratings[i]:
            result[i] = 1
        elif ratings[i - 1] >= ratings[i]:
            result[i] = 1

            for j in range(i, 0, -1):
                if ratings[j - 1] > ratings[j]:
                    if result[j - 1] > result[j]:
                        break
                    elif result[j - 1] == result[j]:
                        result[j - 1] += 1
                    elif result[j - 1] < result[j]:
                        result[j - 1] = result[j] + 1
                elif ratings[j - 1] == ratings[j]:
                    break
                elif ratings[j - 1] < ratings[j]:
                    if result[j - 1] > result[j]:
                        result[j] = result[j - 1] + 1
                    else:
                        break

    return sum(result)


# One Pass Approach
# With memorization of where was last increase before decrease sequence
# Time: O(n)
# Space: O(1)
def solution_2(ratings: list[int]) -> int:
    result = 1

    prev_val = 1
    last_increase = 0
    last_increase_val = 0
    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            result += prev_val + 1
            prev_val = prev_val + 1
            last_increase = i
            last_increase_val = prev_val
        elif ratings[i - 1] == ratings[i]:
            result += 1
            prev_val = 1
            last_increase = i
            last_increase_val = prev_val
        elif ratings[i - 1] >= ratings[i]:
            if prev_val == 1:
                result += (i - last_increase - 1) + 1
                if i - last_increase >= last_increase_val:
                    result += 1
                prev_val = 1
            else:
                result += 1
                prev_val = 1

    return result


# Two Pass Approach: 
# 1. From left to right
# 2. From right to left
# Time: O(n)
# Space: O(n)
def solution_3(ratings: list[int]) -> int:
    candies = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
    
    return sum(candies)


class _Data(NamedTuple):
    ratings: list[int]


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            ratings=[1,0,2],
        ),
        expected=5,
    ),
    TestCase(
        params=_Data(
            ratings=[1,2,2],
        ),
        expected=4,
    ),
    TestCase(
        params=_Data(
            ratings=[1,2,3,4,5,6,7,8],
        ),
        expected=36,
    ),
    TestCase(
        params=_Data(
            ratings=[6,5,4,3,2,1],
        ),
        expected=21,
    ),
    TestCase(
        params=_Data(
            ratings=[1, 2, 3, 2, 1, 2, 3, 2, 1],
        ),
        expected=17,
    ),
    TestCase(
        params=_Data(
            ratings=[1,3,2,2,1],
        ),
        expected=7,
    ),
    TestCase(
        params=_Data(
            ratings=[1,3,4,5,2],
        ),
        expected=11,
    ),
]


profile_solutions([solution_1, solution_2, solution_3], test_cases)

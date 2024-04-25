# Medium

# Topics: Array, Heap(Priority Queue) 

# Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums

# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 104
# k <= nums1.length * nums2.length


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase
from heapq import heappop, heappush


# Using Heap Queue
# Time: O(k * log(n))
# Space: O(k)
def solution_1(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    n, m = len(nums1), len(nums2)
    hp = [(nums1[0] + nums2[0], 0, 0)]
    result = []

    visited = set()
    visited.add((0, 0))

    while len(result) < k and len(hp) > 0:
        _, i, j = heappop(hp)
        result.append([nums1[i], nums2[j]])

        if i < n - 1 and (i + 1, j) not in visited:
            heappush(hp, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))
        if j < m - 1 and (i, j + 1) not in visited:
            heappush(hp, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))
    return result


class _Data(NamedTuple):
    nums1: list[int]
    nums2: list[int]
    k: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            nums1=[1,7,11],
            nums2=[2,4,6],
            k=3,
        ),
        expected=[[1,2],[1,4],[1,6]],
    ),
    TestCase(
        params=_Data(
            nums1=[1,1,2],
            nums2=[1,2,3],
            k=2,
        ),
        expected=[[1,1],[1,1]],
    ),
    TestCase(
        params=_Data(
            nums1=[2,4,6],
            nums2=[1,7,11],
            k=3,
        ),
        expected=[[2,1],[4,1],[6,1]],
    ),
    TestCase(
        params=_Data(
            nums1=[1,2,4,5,6],
            nums2=[3,5,7,9],
            k=3,
        ),
        expected=[[1,3],[2,3],[1,5]],
    ),
    TestCase(
        params=_Data(
            nums1=[1,2,4,5,6],
            nums2=[3,5,7,9],
            k=20,
        ),
        expected=[[1,3],[2,3],[1,5],[2,5],[4,3],[1,7],[5,3],[2,7],[4,5],[6,3],[1,9],[5,5],[2,9],[4,7],[6,5],[5,7],[4,9],[6,7],[5,9],[6,9]],
    ),
]


profile_solutions(
    [
        solution_1,
    ], 
    test_cases,
)

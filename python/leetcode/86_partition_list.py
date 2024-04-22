# Medium

# Topics: Linked List, Two Pointers

# Link: https://leetcode.com/problems/partition-list

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.


# Example 1:

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]


# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


from typing import NamedTuple

from infra.asserts import profile_solutions, TestCase
from data_structures import ListNode, list_to_linked_list, linked_list_to_list


# Naive Iterative 
# Time: O(n)
# Space: O(n)
def solution_1(head: ListNode | None, x: int) -> list[int] | None:
    if head is None:
        return None

    less_head = None
    less_current = None

    more_head = None
    more_current = None


    current_node = head
    while current_node:
        if current_node.val < x:
            if less_head is None:
                less_head = ListNode(
                    val=current_node.val
                )
                less_current = less_head
            else:
                less_current.next = ListNode(
                    val=current_node.val,
                )
                less_current = less_current.next
        else:
            if more_head is None:
                more_head = ListNode(
                    val=current_node.val
                )
                more_current = more_head
            else:
                more_current.next = ListNode(
                    val=current_node.val,
                )
                more_current = more_current.next
        current_node = current_node.next

    if less_head is None:
        return linked_list_to_list(more_head)
    
    less_current.next = more_head
    return linked_list_to_list(less_head)


# In-Place Iterative 
# Time: O(n)
# Space: O(1)
def solution_2(head: ListNode | None, x: int) -> list[int] | None:
    less_head = None
    less_tail = None
    more_head = None
    more_tail = None

    cur = head
    while cur:
        if cur.val < x:
            if less_head is None:
                less_head = cur
                less_tail = cur
            else:
                less_tail.next = cur
                less_tail = less_tail.next
        else:
            if more_head is None:
                more_head = cur
                more_tail = cur
            else:
                more_tail.next = cur
                more_tail = more_tail.next
        cur = cur.next
    
    if more_head and less_tail:
        less_tail.next = more_head
        more_tail.next = None
    elif less_tail:
        less_tail.next = None
    
    if not less_tail:
        return linked_list_to_list(more_head)
    
    return linked_list_to_list(less_head)


class _Data(NamedTuple):
    head: ListNode | None
    x: int


test_cases: list[TestCase[_Data]] = [
    TestCase(
        params=_Data(
            head=list_to_linked_list([1,4,3,2,5,2]),
            x=3,
        ),
        expected=[1,2,2,4,3,5],
    ),
    TestCase(
        params=_Data(
            head=list_to_linked_list([2,1]),
            x=2,
        ),
        expected=[1,2],
    ),
    TestCase(
        params=_Data(
            head=list_to_linked_list([1]),
            x=0,
        ),
        expected=[1],
    ),
]


profile_solutions(
    [
        solution_1,
        solution_2, 
    ], 
    test_cases,
)

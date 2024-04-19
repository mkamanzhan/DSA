# Medium

# Topics: Stack, Design

# Link: https://leetcode.com/problems/min-stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


class Node:

    def __init__(self, val: int, min_val: int, next = None,) -> None:
        self.val = val
        self.min_val = min_val
        self.next = next


class MinStack:

    def __init__(self):
        self._head = None

    def push(self, val: int) -> None:
        if self._head is None:
            self._head = Node(
                val=val,
                min_val=val,
            )
            return None
        
        min_val = self._head.min_val
        if val < min_val:
            min_val = val
        self._head = Node(
            val=val,
            min_val=min_val,
            next=self._head,
        )

    def pop(self) -> int | None:
        if self._head is None:
            return None
        
        val = self._head.val
        self._head = self._head.next
        return val

    def top(self) -> int | None:
        if self._head is None:
            return None
        return self._head.val

    def getMin(self) -> int | None:
        if self._head is None:
            return None

        return self._head.min_val


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())

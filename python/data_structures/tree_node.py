from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree_node(nums: list[int | None]) -> TreeNode | None:
    if not nums:
        return None
    
    if nums[0] is None:
        return None

    root = TreeNode(val=nums[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nums):
        node = queue.popleft()

        if nums[i] is not None:
            node.left = TreeNode(val=nums[i])
            queue.append(node.left)

        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(val=nums[i])
            queue.append(node.right)

        i += 1

    return root


def tree_node_to_list(head: TreeNode):
    if not head:
        return []

    queue = deque([head])
    result = []

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    return result

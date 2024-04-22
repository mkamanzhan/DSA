class ListNode:
    def __init__(self, val: int, next = None) -> None:
        self.val = val
        self.next = next
    

def list_to_linked_list(nums: list[int]) -> ListNode:
    head = ListNode(val=nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(val=i)
        node = node.next
    return head


def linked_list_to_list(head: ListNode) -> list[int]:
    node = head
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

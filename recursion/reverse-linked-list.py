# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr_return_node = ListNode(head.val, None)
        curr_node = head.next
        while curr_node is not None:
            curr_return_node = ListNode(curr_node.val, curr_return_node)
            curr_node = curr_node.next
        return curr_return_node

        
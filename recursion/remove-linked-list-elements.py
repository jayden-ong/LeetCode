# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr_head = head
        while curr_head is not None and curr_head.val == val:
            curr_head = curr_head.next
        
        if curr_head is None:
            return None
        
        prev = curr_head
        # There is only one element left of the list that does not have value val
        if prev.next is None:
            return curr_head
        
        curr_node = prev.next
        while curr_node is not None:
            if curr_node.val == val:
                prev.next = curr_node.next
                curr_node = prev.next
            else:
                prev = curr_node
                curr_node = curr_node.next

        return curr_head
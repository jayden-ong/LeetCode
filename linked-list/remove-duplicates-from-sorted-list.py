# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
            
        curr_head = head
        item_to_check = head.next
        while item_to_check is not None:
            if item_to_check.val != curr_head.val:
                curr_head.next = item_to_check
                curr_head = item_to_check
            item_to_check = item_to_check.next
        curr_head.next = None
        return head
        
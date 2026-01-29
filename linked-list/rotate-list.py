# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr = head
        list_length = 0
        while curr is not None:
            curr = curr.next
            list_length += 1
        
        k = k % list_length
        if k == 0 or list_length <= 1:
            return head

        
        # Want to keep track of old head
        old_head = head
        curr = head
        nodes_encountered = 1
        while nodes_encountered < list_length - k:
            curr = curr.next
            nodes_encountered += 1
        # When loop ends, curr will be the end of the list
        new_head = curr.next
        curr.next = None
        new_curr = new_head
        while new_curr.next is not None:
            new_curr = new_curr.next
        new_curr.next = old_head
        return new_head
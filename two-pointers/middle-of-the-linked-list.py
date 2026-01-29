# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            curr_length += 1
        
        middle_index = curr_length // 2
        curr = head
        curr_pos = 0
        while curr is not None:
            if curr_pos == middle_index:
                return curr
            curr_pos += 1
            curr = curr.next

        
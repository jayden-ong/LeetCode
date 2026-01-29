# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_answer = None
        curr_seg = None
        # Beginning of list is always 0
        curr = head.next
        curr_sum = 0
        while curr is not None:
            if curr.val == 0:
                if curr_answer is None:
                    curr_answer = ListNode(curr_sum, None)
                    curr_seg = curr_answer
                else:
                    curr_seg.next = ListNode(curr_sum, None)
                    curr_seg = curr_seg.next
                curr_sum = 0
            else:
                curr_sum += curr.val
            curr = curr.next
        return curr_answer
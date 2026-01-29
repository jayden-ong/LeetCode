# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        answer = head
        prev = None
        new_head = False
        while curr is not None and curr.next is not None:
            temp1 = curr.next
            temp2 = curr
            curr.next = curr.next.next
            temp1.next = temp2
            if not new_head:
                answer = temp1
                new_head = True
            if prev is not None:
                prev.next = temp1
            prev = curr
            curr = curr.next
            #print(answer)
            #print(curr)
        return answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp_A = headA
        temp_B = headB
        while temp_A != temp_B:
            if temp_A is None:
                temp_A = headB
            else:
                temp_A = temp_A.next

            if temp_B is None:
                temp_B = headA
            else:
                temp_B = temp_B.next
        
        return temp_A
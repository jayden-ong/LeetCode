# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_curr = l1
        second_curr = l2
        result_head = ListNode(0, None)
        result_curr = result_head
        carry_over = 0
        while first_curr is not None or second_curr is not None:
            curr_val = 0
            if first_curr is not None:
                curr_val += first_curr.val
                first_curr = first_curr.next
            if second_curr is not None:
                curr_val += second_curr.val
                second_curr = second_curr.next
            
            carry_over = 0
            if curr_val + result_curr.val >= 10:
                carry_over = 1
                curr_val -= 10
            result_curr.val += curr_val
            if first_curr is not None or second_curr is not None or carry_over != 0:
                result_curr.next = ListNode(carry_over, None)
                result_curr = result_curr.next
        
        return result_head
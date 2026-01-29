# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(first_num, second_num):
            for i in range(min(first_num, second_num), 0, -1):
                if first_num % i == 0 and second_num % i == 0:
                    return i
        
        if head is None or head.next is None:
            return head
        
        first_num = head.val
        answer = ListNode(first_num, None)
        curr_answer = answer
        curr = head.next
        while curr is not None:
            # Need to create the gcd node
            second_num = curr.val
            curr_gcd = gcd(first_num, second_num)
            # Create gcd node
            curr_answer.next = ListNode(curr_gcd, None)
            curr_answer = curr_answer.next
            # Create other node
            curr_answer.next = ListNode(second_num, None)
            curr_answer = curr_answer.next
            # Update current node and first_num for next iteration
            first_num = second_num
            curr = curr.next
        return answer
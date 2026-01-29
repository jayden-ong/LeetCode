# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        curr = head
        num_digits = 0
        while curr is not None:
            num.append(curr.val)
            curr = curr.next
            num_digits += 1
        
        double_num = []
        carry_over = 0
        for i in range(num_digits - 1, -1, -1):
            res = (2 * num[i]) + carry_over
            double_num = [res % 10] + double_num
            carry_over = res // 10
        if carry_over == 1:
            double_num = [1] + double_num
        
        answer = None
        for num in double_num:
            if answer is None:
                answer = ListNode(num, None)
                curr = answer
            else:
                new_node = ListNode(num, None)
                curr.next = new_node
                curr = curr.next
        return answer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        vals_list = []
        while curr is not None:
            vals_list.append(curr.val)
            curr = curr.next
        
        num_vals = len(vals_list)
        for i in range(num_vals // 2):
            if vals_list[i] != vals_list[num_vals - i - 1]:
                return False
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        string_binary = ""
        curr = head
        while curr is not None:
            string_binary += str(curr.val)
            curr = curr.next
        
        return int(string_binary, 2)
        

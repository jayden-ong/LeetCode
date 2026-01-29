# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes_list = []
        i = 1
        curr = head
        while curr is not None and i <= right:
            if i >= left and i <= right:
                nodes_list.append(curr)
            i += 1
            curr = curr.next
        
        right -= left
        left = 0
        while left < right:
            temp = nodes_list[left].val
            nodes_list[left].val = nodes_list[right].val
            nodes_list[right].val = temp
            left += 1
            right -= 1
        return head
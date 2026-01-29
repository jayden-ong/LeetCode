# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nodes_seen = [head]
        while curr is not None:
            curr = curr.next
            if curr in nodes_seen:
                return curr
            else:
                nodes_seen.append(curr)
        return None
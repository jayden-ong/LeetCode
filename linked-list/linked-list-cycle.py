# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        nodes_visited = []
        curr_node = head
        while True:
            if curr_node in nodes_visited:
                return True
            elif curr_node.next is None:
                return False
            nodes_visited.append(curr_node)
            curr_node = curr_node.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head is guarenteed not to be none
        # Want to get the length
        curr = head
        list_length = 0
        while curr is not None:
            curr = curr.next
            list_length += 1
        
        if n == list_length:
            node_to_return = head.next
            return node_to_return
        # Want to remove the list_length - nth index
        # There are a few possibilities:
        #   Want to remove the last node
        nodes_to_consider = []
        num_nodes_to_consider = 0
        curr = head
        node_index = 0
        node_to_remove = list_length - n
        while curr is not None:
            if node_to_remove - 1 <= node_index and node_index <= node_to_remove + 1:
                nodes_to_consider.append(curr)
                num_nodes_to_consider += 1
            curr = curr.next
            node_index += 1
        
        if num_nodes_to_consider == 3:
            nodes_to_consider[0].next = nodes_to_consider[2]
        elif num_nodes_to_consider == 2:
            nodes_to_consider[0].next = None
        return head
        
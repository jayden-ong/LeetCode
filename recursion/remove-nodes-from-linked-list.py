# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value_list = []
        curr = head
        num_vals = 0
        while curr is not None:
            value_list.append(curr.val)
            curr = curr.next
            num_vals += 1
        
        if num_vals == 1:
            return curr
        # Want to figure out which nodes to remove
        removal_set = set()
        curr_greatest = value_list[num_vals - 1]
        for i in range(num_vals - 2, -1, -1):
            # Remove index i from linked list
            if value_list[i] < curr_greatest:
                removal_set.add(i)
            elif value_list[i] > curr_greatest:
                curr_greatest = value_list[i]
        
        curr = head
        i = 0
        answer = None
        actual_answer = None
        while curr is not None:
            if i not in removal_set:
                if answer is None:
                    answer = ListNode(curr.val, None)
                    actual_answer = answer
                else:
                    new_node = ListNode(curr.val, None)
                    answer.next = new_node
                    answer = answer.next
            curr = curr.next
            i += 1
        return actual_answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        # Want to store all the heads of all the lists and their value
        heads_list = []
        values_list = []
        num_lists = 0
        smallest = None
        index_of_smallest = 0
        num_none = 0
        for head in lists:
            heads_list.append(head)
            if head is None:
                num_none += 1
                values_list.append(math.inf)
            else:
                values_list.append(head.val)
                if smallest is None or head.val < smallest:
                    smallest = head.val
                    index_of_smallest = num_lists
            num_lists += 1
        
        # Want to keep track of how many None there are in the list of heads
        # Will stop once all heads are none
        if num_none == num_lists:
            return None
        
        curr_res_head = ListNode(values_list[index_of_smallest], None)
        curr_res = curr_res_head
        heads_list[index_of_smallest] = heads_list[index_of_smallest].next
        if heads_list[index_of_smallest] is None:
            values_list[index_of_smallest] = math.inf
            num_none += 1
        else:
            values_list[index_of_smallest] = heads_list[index_of_smallest].val
        while num_none != num_lists:
            smallest = values_list[0]
            index_of_smallest = 0
            for i in range(1, num_lists):
                if values_list[i] < smallest:
                    smallest = values_list[i]
                    index_of_smallest = i
            curr_res.next = ListNode(values_list[index_of_smallest], None)
            heads_list[index_of_smallest] = heads_list[index_of_smallest].next
            if heads_list[index_of_smallest] is None:
                values_list[index_of_smallest] = math.inf
                num_none += 1
            else:
                values_list[index_of_smallest] = heads_list[index_of_smallest].val
            curr_res = curr_res.next
        return curr_res_head
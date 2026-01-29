# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = []
        for i in range(k):
            answer.append(None)        
        # Want to get length of linked list
        list_len = 0
        curr = head
        while curr is not None:
            list_len += 1
            curr = curr.next
        
        # Amount each component must have at minimum
        min_length = list_len // k
        leftover = list_len % k
        curr = head
        j = 0
        while curr is not None:
            desired_length = min_length
            curr_head = curr
            if leftover > 0:
                desired_length += 1
                leftover -= 1

            for i in range(desired_length - 1):
                curr = curr.next
            
            temp = curr.next
            curr.next = None
            curr = temp
            answer[j] = curr_head
            j += 1
        return answer
        
        
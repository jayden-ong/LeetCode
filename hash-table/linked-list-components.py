# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        answer = 0
        nums = set(nums)
        curr = head
        streak = 0
        while curr is not None:
            if curr.val in nums:
                streak += 1
                if curr.next is None:
                    answer += 1
            else:
                if streak > 0:
                    answer += 1
                streak = 0
            curr = curr.next
        return answer
                

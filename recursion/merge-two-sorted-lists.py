# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        curr_head = None
        curr_res = None
        while curr1 is not None or curr2 is not None:
            if curr_head is None:
                if curr1 is None:
                    curr_head = ListNode(curr2.val, None)
                    curr2 = curr2.next
                elif curr2 is None:
                    curr_head = ListNode(curr1.val, None)
                    curr1 = curr1.next
                else:
                    if curr1.val < curr2.val:
                        curr_head = ListNode(curr1.val, None)
                        curr1 = curr1.next
                    else:
                        curr_head = ListNode(curr2.val, None)
                        curr2 = curr2.next
                curr_res = curr_head
            else:
                if curr1 is None:
                    curr_res.next = ListNode(curr2.val, None)
                    curr2 = curr2.next
                elif curr2 is None:
                    curr_res.next = ListNode(curr1.val, None)
                    curr1 = curr1.next
                else:
                    if curr1.val < curr2.val:
                        curr_res.next = ListNode(curr1.val, None)
                        curr1 = curr1.next
                    else:
                        curr_res.next = ListNode(curr2.val, None)
                        curr2 = curr2.next
                curr_res = curr_res.next
        return curr_head
        
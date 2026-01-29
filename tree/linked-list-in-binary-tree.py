# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        new_list = []
        curr = head
        while curr:
            new_list.append(curr.val)
            curr = curr.next
        
        candidates = []
        def find_starting_nodes(root):
            if root is None:
                return
            
            if root.val == new_list[0]:
                candidates.append(root)
            
            find_starting_nodes(root.left)
            find_starting_nodes(root.right)
        
        def find_path(root, curr_index):
            if curr_index == len(new_list):
                return True
            
            if root is None:
                return False
            
            if root.val == new_list[curr_index]:
                if find_path(root.left, curr_index + 1) or find_path(root.right, curr_index + 1):
                    return True
            return False

        find_starting_nodes(root)
        for candidate in candidates:
            if find_path(candidate, 0):
                return True
        return False

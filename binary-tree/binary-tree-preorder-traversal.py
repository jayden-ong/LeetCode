# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr_list = []
        if root is None:
            return curr_list
        
        curr_list.append(root.val)
        curr_list.extend(self.preorderTraversal(root.left))
        curr_list.extend(self.preorderTraversal(root.right))
        return curr_list
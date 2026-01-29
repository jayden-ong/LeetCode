# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr_list = []
        if root is not None:
            curr_list.extend(self.inorderTraversal(root.left))
            curr_list.append(root.val)
            curr_list.extend(self.inorderTraversal(root.right))
        return curr_list
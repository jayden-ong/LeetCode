# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        
        if root2 is None:
            return root1
        
        # No matter what, the new root value will be root1.val + root2.val
        new_root = TreeNode(root1.val + root2.val, None, None)
        if root1.left is None or root2.left is None:
            if root1.left is None:
                new_left = root2.left
            else:
                new_left = root1.left
        else:
            new_left = self.mergeTrees(root1.left, root2.left)
        
        if root1.right is None or root2.right is None:
            if root1.right is None:
                new_right = root2.right
            else:
                new_right = root1.right
        else:
            new_right = self.mergeTrees(root1.right, root2.right)
        
        new_root.left = new_left
        new_root.right = new_right
        return new_root
        
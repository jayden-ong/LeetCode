# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            if root.val == target:
                return None
            else:
                return root
        
        new_left = self.removeLeafNodes(root.left, target)
        new_right = self.removeLeafNodes(root.right, target)
    
        if new_left is not None and new_left.left is None and new_left.right is None and new_left.val == target:
            new_left = None
        
        if new_right is not None and new_right.left is None and new_right.right is None and new_right.val == target:
            new_right = None
        
        if new_left is None and new_right is None and root.val == target:
            return None
        root.left = new_left
        root.right = new_right
        return root
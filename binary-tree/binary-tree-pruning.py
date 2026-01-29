# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def remove_zeros(root):
            if root is None:
                return None
            
            if root.left is None and root.right is None:
                if root.val == 1:
                    return root
                return None
            
            # Want to alter the left and right
            new_left = remove_zeros(root.left)
            new_right = remove_zeros(root.right)

            root.left = new_left
            root.right = new_right
            if root.val == 1:
                return root
            
            if new_left is None and new_right is None:
                return None
            return root
        return remove_zeros(root)
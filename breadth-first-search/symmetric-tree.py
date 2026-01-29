# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym_helper(root1: Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
            if root1 is None and root2 is None:
                return True
            elif root1 is None and root2 is not None:
                return False
            elif root1 is not None and root2 is None:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return sym_helper(root1.left, root2.right) and sym_helper(root1.right, root2.left)
        
        return sym_helper(root.left, root.right)
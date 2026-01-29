# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(root):
            if root is None:
                return None
            # Means nothing in the left side of the tree
            if root.val < low:
                return trim(root.right)
            # Means nothing in the right side of the tree
            elif root.val > high:
                return trim(root.left)
            
            # Root stays and have to modify both sides of the tree
            root.left = trim(root.left)
            root.right = trim(root.right)
            return root
        
        return trim(root)
        
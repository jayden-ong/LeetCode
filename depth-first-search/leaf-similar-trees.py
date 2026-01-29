# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find_leaf_sequence(root):
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                return [root.val]
            
            return find_leaf_sequence(root.left) + find_leaf_sequence(root.right)
        
        return find_leaf_sequence(root1) == find_leaf_sequence(root2)
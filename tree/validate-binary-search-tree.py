# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # For each node, check the current children
        if root.left is not None and root.left.val >= root.val:
            return False
        
        if root.right is not None and root.right.val <= root.val:
            return False
        
        if root.left is not None and not self.isValidBST(root.left):
            return False
        
        if root.right is not None and not self.isValidBST(root.right):
            return False
        
        # Check the rightmost child in left subtree
        if root.left is not None:
            curr_node = root.left
            curr_val = root.left.val
            while curr_node.right is not None:
                curr_node = curr_node.right
                curr_val = curr_node.val
            
            if curr_val >= root.val:
                return False
        
        # Check the leftmost child in right subtree
        if root.right is not None:
            curr_node = root.right
            curr_val = root.right.val
            while curr_node.left is not None:
                curr_node = curr_node.left
                curr_val = curr_node.val
            
            if curr_val <= root.val:
                return False
        return True
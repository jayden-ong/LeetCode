# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Need to take everything on the left, move it to the right
        # Take everything on the right and attach it to end of left
        def helper(curr_node):
            if curr_node is None:
                return None
            
            if curr_node.left is None and curr_node.right is None:
                return curr_node
            
            # Want to store the current subtrees
            curr_right = curr_node.right
            curr_left = curr_node.left
            # Need to "fix" the left subtree 
            helper(curr_left)
            # Need to remove the entire left subtree and put the "fixed" on to the right 
            curr_node.right = curr_left
            curr_node.left = None
            # Need last node on the right
            last_chain_node = curr_node
            while last_chain_node.right is not None:
                last_chain_node = last_chain_node.right
            helper(curr_right)
            last_chain_node.right = curr_right
            return
        helper(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def longest_path(root, parent_val):
            # Only self.answer will deal with nodes from two different subtrees
            if root is None:
                return 0
            
            left = longest_path(root.left, root.val)
            right = longest_path(root.right, root.val)

            self.answer = max(self.answer, left + right)
            # Means we can combine into consec path
            if parent_val is not None and parent_val == root.val:
                return max(left, right) + 1
            
            return 0
        
        longest_path(root, None)
        return self.answer

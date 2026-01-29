# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # The first index stores the max money if you rob the root
        # The second index store the max money if you don't rob the root
        def recursive(root):
            if root.left is None and root.right is None:
                return (root.val, 0)
            
            results_left = (0, 0)
            if root.left is not None:
                results_left = recursive(root.left)
            
            results_right = (0, 0)
            if root.right is not None:
                results_right = recursive(root.right)
            
            # If I rob the root, have to use second index of results
            return (root.val + results_left[1] + results_right[1], max(results_left[0], results_left[1]) + max(results_right[0], results_right[1]))


        results = recursive(root)
        return max(results[0], results[1])
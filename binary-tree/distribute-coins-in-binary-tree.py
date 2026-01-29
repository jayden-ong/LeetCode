# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Return value stores number of moves, number of coins
        def helper(root):
            if root.left is None and root.right is None:
                return (abs(root.val - 1), root.val - 1)
            
            left_data = (0, 0)
            if root.left is not None:
                left_data = helper(root.left)
            
            right_data = (0, 0)
            if root.right is not None:
                right_data = helper(root.right)
            
            return (abs(root.val - 1 + left_data[1] + right_data[1]) + left_data[0] + right_data[0], root.val - 1 + left_data[1] + right_data[1])
        
        return helper(root)[0]

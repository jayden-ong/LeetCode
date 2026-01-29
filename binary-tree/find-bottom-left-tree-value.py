# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # To find the left most in last row, need to determine depth of last row
        def find_bottom_left_value(root, curr_depth):
            if root.left is None and root.right is None:
                return (root.val, curr_depth)
            
            first_cand = (0, 0)
            if root.left is not None:
                first_cand = find_bottom_left_value(root.left, curr_depth + 1)
            
            second_cand = (0, 0)
            if root.right is not None:
                second_cand = find_bottom_left_value(root.right, curr_depth + 1)
            
            if first_cand[1] >= second_cand[1]:
                return first_cand
            return second_cand
        
        return find_bottom_left_value(root, 0)[0]
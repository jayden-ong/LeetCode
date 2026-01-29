# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        # Need to get the sum of subtrees and sum up tilts
        def find_sum_tilts(root):
            if root is None:
                return (0, 0)
            if root.left is None and root.right is None:
                return (root.val, 0)
            
            sum_left, tilt_left = find_sum_tilts(root.left)
            sum_right, tilt_right = find_sum_tilts(root.right)
            return (sum_left + sum_right + root.val, abs(sum_right - sum_left) + tilt_left + tilt_right)


        return find_sum_tilts(root)[1]

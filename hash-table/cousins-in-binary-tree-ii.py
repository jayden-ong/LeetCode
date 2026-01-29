# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Get the sum of all levels
        level_sums = []
        def get_sum(root, curr_level):
            if curr_level >= len(level_sums):
                level_sums.append(root.val)
            else:
                level_sums[curr_level] += root.val
            
            if root.left is not None:
                get_sum(root.left, curr_level + 1)
            
            if root.right is not None:
                get_sum(root.right, curr_level + 1)
        
        def set_new_vals(root, curr_level):
            if root is None or (root.left is None and root.right is None):
                return
            
            # Get new val
            curr_val = level_sums[curr_level + 1]
            if root.right is not None:
                curr_val -= root.right.val
            
            if root.left is not None:
                curr_val -= root.left.val
            
            # Set new val
            if root.right is not None:
                root.right.val = curr_val
                set_new_vals(root.right, curr_level + 1)
            
            if root.left is not None:
                root.left.val = curr_val
                set_new_vals(root.left, curr_level + 1)

        get_sum(root, 0)
        
        # By default, the root is always going to be 0
        root.val = 0
        set_new_vals(root, 0)
        return root
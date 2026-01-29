# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def get_depth_parent_val(root, desired_val, curr_depth, curr_parent):
            if root is None:
                return None
            
            if root.val == desired_val:
                if curr_parent is None:
                    return (curr_depth, None)
                return (curr_depth, curr_parent.val)
            
            if root.left is None:
                return get_depth_parent_val(root.right, desired_val, curr_depth + 1, root)
            
            if root.right is None:
                return get_depth_parent_val(root.left, desired_val, curr_depth + 1, root)
            
            left = get_depth_parent_val(root.left, desired_val, curr_depth + 1, root)
            right = get_depth_parent_val(root.right, desired_val, curr_depth + 1, root)
            if left:
                return left
            return right
        
        x_location = get_depth_parent_val(root, x, 0, None)
        y_location = get_depth_parent_val(root, y, 0, None)
        if x_location and y_location:
            return x_location[0] == y_location[0] and x_location[1] != y_location[1]
        return False
            
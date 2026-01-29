# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # Assume left is initially passed in
        def get_largest_left(root):
            if root.right is None:
                return root.val
            else:
                return get_largest_left(root.right)
        
        def get_smallest_right(root):
            if root.left is None:
                return root.val
            else:
                return get_smallest_right(root.left)
        
        curr_cand = []
        smallest_diff_left = None
        largest_left = None
        if root.left is not None:
            largest_left = get_largest_left(root.left)
            curr_cand.append(abs(root.val - largest_left))
            # Have to ensure there are at least two nodes when we call the function
            if root.left.left is not None or root.left.right is not None:
                smallest_diff_left = self.getMinimumDifference(root.left)
                curr_cand.append(smallest_diff_left)
        
        smallest_diff_right = None
        smallest_right = None
        if root.right is not None:
            smallest_right = get_smallest_right(root.right)
            curr_cand.append(abs(root.val - smallest_right))
            if root.right.left is not None or root.right.right is not None:
                smallest_diff_right = self.getMinimumDifference(root.right)
                curr_cand.append(smallest_diff_right)
        
        return min(curr_cand)
        
        
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(root, curr_sum):
            if root.left is None and root.right is None:
                root.val += curr_sum
                return root.val
            
            # Start with right
            if root.right is not None:
                all_greater_sum = recursive(root.right, curr_sum)
                root.val += all_greater_sum
            else:
                root.val += curr_sum
            
            if root.left is not None:
                sum_greater = recursive(root.left, root.val)
                return sum_greater
            return root.val
        
        if root is not None:
            recursive(root, 0)
        return root
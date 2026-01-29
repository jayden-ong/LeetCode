# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recursive(root, curr_sum):
            if root.left is None and root.right is None:
                root.val += curr_sum
                return root.val
            
            greater_sum = 0
            if root.right is not None:
                greater_sum += recursive(root.right, curr_sum)
                root.val += greater_sum
            else:
                root.val += curr_sum
            
            if root.left is not None:
                return recursive(root.left, root.val)
            return root.val

        recursive(root, 0)
        return root
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def find_target(root, target):
            if root is None:
                return None
            
            if root.val == target:
                return root
            
            target_left = find_target(root.left, target)
            target_right = find_target(root.right, target)
            if target_left:
                return target_left
            elif target_right:
                return target_right
            else:
                return None
        
        return find_target(cloned, target.val)
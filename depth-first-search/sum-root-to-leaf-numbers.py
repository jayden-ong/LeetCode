# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def stringifyNumbers(root):
            if root is None:
                return []
            
            if root.right is None and root.left is None:
                return [str(root.val)]
            
            all_vals = stringifyNumbers(root.left) + stringifyNumbers(root.right)
            final_ans = []
            string_prepend = str(root.val)
            for val in all_vals:
                final_ans.append(string_prepend + val)

            return final_ans
        
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.val
        
        all_vals = stringifyNumbers(root)
        final_val = 0
        for val in all_vals:
            final_val += int(val)
        
        return final_val
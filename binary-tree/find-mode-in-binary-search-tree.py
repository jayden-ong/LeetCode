# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def num_occurrences(root):
            if root is None:
                return {}
            
            if root.left is None and root.right is None:
                return {root.val : 1}
            
            left_dict = num_occurrences(root.left)
            right_dict = num_occurrences(root.right)
            final_dict = {}

            for key in left_dict:
                final_dict[key] = left_dict[key] + right_dict.get(key, 0)
            
            for key in right_dict:
                if final_dict.get(key, -1) == -1:
                    final_dict[key] = right_dict[key]
            
            final_dict[root.val] = final_dict.get(root.val, 0) + 1
            return final_dict
        
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        occurr_dict = num_occurrences(root)
        curr_ans = []
        curr_max = 0
        for key in occurr_dict:
            if occurr_dict[key] == curr_max:
                curr_ans.append(key)
            elif occurr_dict[key] > curr_max:
                curr_max = occurr_dict[key]
                curr_ans = [key]
        return curr_ans
        

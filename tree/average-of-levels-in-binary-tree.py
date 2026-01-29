# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def get_val_level(root, level):
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                return [(root.val, level)]
            
            left_level = get_val_level(root.left, level + 1)
            right_level = get_val_level(root.right, level + 1)

            curr_res = [(root.val, level)]
            curr_res.extend(left_level)
            curr_res.extend(right_level)
            return curr_res
        
        vals_levels_list = get_val_level(root, 0)
        # Key is the level and value is [curr_val, num]
        levels_dict = {}
        max_level = -1
        for (val, level) in vals_levels_list:
            if level not in levels_dict:
                levels_dict[level] = [val, 1]
            else:
                levels_dict[level][0] += val
                levels_dict[level][1] += 1
            max_level = max(max_level, level)
        
        curr_answer = [0] * (max_level + 1)
        for i in range(max_level + 1):
            curr_answer[i] = levels_dict[i][0] / levels_dict[i][1]
        return curr_answer
        

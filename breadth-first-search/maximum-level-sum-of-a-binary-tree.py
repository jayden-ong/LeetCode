# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels_dict = defaultdict(int)
        def update_dict(root, curr_level):
            levels_dict[curr_level] += root.val
            if root.left is not None:
                update_dict(root.left, curr_level + 1)
            if root.right is not None:
                update_dict(root.right, curr_level + 1)
        
        update_dict(root, 1)
        answer, curr_best = 1, levels_dict[1]
        for level in levels_dict:
            if levels_dict[level] > curr_best:
                answer, curr_best = level, levels_dict[level]
        return answer
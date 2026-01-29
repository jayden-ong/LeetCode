# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        def calc_level_sums(root, curr_level):
            if curr_level >= len(level_sums):
                level_sums.append(root.val)
            else:
                level_sums[curr_level] += root.val
            
            if root.left is not None:
                calc_level_sums(root.left, curr_level + 1)
            
            if root.right is not None:
                calc_level_sums(root.right, curr_level + 1)
        
        calc_level_sums(root, 0)
        if k - 1 >= len(level_sums):
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]

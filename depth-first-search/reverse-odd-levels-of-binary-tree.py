# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        odd_levels_dict = defaultdict(list)
        def reverse_nodes(root, level):
            if level % 2 == 1:
                odd_levels_dict[level].append((root, root.val))
            
            if root.left is not None:
                reverse_nodes(root.left, level + 1)
                reverse_nodes(root.right, level + 1)
                
        reverse_nodes(root, 0)
        for level in odd_levels_dict:
            for i in range(len(odd_levels_dict[level])):
                curr_root, _ = odd_levels_dict[level][i]
                curr_root.val = odd_levels_dict[level][len(odd_levels_dict[level]) - i - 1][1]
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        tree_values = defaultdict(list)
        def extract_values(root, level):
            tree_values[level].append(root.val)
            if root.left is not None:
                extract_values(root.left, level + 1)
            
            if root.right is not None:
                extract_values(root.right, level + 1)
        
        extract_values(root, 0)
        answer = 0
        for level in tree_values:
            curr_level_values = tree_values[level]
            sorted_values = curr_level_values.copy()
            sorted_values.sort()
            positions_dict = {}
            for i in range(len(curr_level_values)):
                positions_dict[curr_level_values[i]] = i
            
            for i in range(len(curr_level_values)):
                # Have to swap
                if curr_level_values[i] != sorted_values[i]:
                    # Get current position of value that should go here
                    desired_pos = positions_dict[sorted_values[i]]
                    curr_level_values[i], curr_level_values[desired_pos] = sorted_values[i], curr_level_values[i]
                    positions_dict[curr_level_values[desired_pos]] = desired_pos
                    answer += 1
        return answer
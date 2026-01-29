# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(nums_list):
            if len(nums_list) == 0:
                return None
            elif len(nums_list) == 1:
                return TreeNode(nums_list[0], None, None)
            
            # Get max
            nums_max = max(nums_list)
            max_index = nums_list.index(nums_max)
            new_node = TreeNode(nums_max, None, None)
            new_node.left = build_tree(nums_list[:max_index])
            new_node.right = build_tree(nums_list[max_index + 1:])
            return new_node
        
        return build_tree(nums)
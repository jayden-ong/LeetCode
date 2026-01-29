# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def tree_sort(root):
            if root.left is None and root.right is None:
                return [root.val]
            
            first_part = []
            if root.left is not None:
                first_part = tree_sort(root.left)
            
            second_part = []
            if root.right is not None:
                second_part = tree_sort(root.right)
            
            return first_part + [root.val] + second_part
        
        sorted_tree = tree_sort(root)
        
        # Want to make the midpoint the root of the entire tree
        def tree_divide(nums_list):
            if len(nums_list) == 0:
                return None
            elif len(nums_list) == 1:
                return TreeNode(nums_list[0], None, None)
            
            mid = len(nums_list) // 2
            new_node = TreeNode(nums_list[mid], None, None)
            new_node.left = tree_divide(nums_list[:mid])
            new_node.right = tree_divide(nums_list[mid + 1:])
            return new_node
        return tree_divide(sorted_tree)
        

        
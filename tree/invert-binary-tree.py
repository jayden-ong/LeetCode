# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root

        new_root_node = TreeNode(root.val, None, None)

        inverted_left_node = self.invertTree(root.left)
        inverted_right_node = self.invertTree(root.right)
        new_root_node.left = inverted_right_node
        new_root_node.right = inverted_left_node
        return new_root_node
        

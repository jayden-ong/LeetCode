# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        if root is None or (root.left is None and root.right is None):
            return 0
        
        def find_longest_path(root):
            if root is None or (root.left is None and root.right is None):
                return 0
            return max(find_longest_path(root.left), find_longest_path(root.right)) + 1
        
        # Need to find diameter of the subtrees
        diam_left = self.diameterOfBinaryTree(root.left)
        diam_right = self.diameterOfBinaryTree(root.right)
        # Need to find longest path to root
        add_factor = 0
        if root.left is not None:
            add_factor += 1
        if root.right is not None:
            add_factor += 1

        longest_left = find_longest_path(root.left)
        longest_right = find_longest_path(root.right)
        all_cand = [diam_left, diam_right, longest_left + longest_right + add_factor]
        return max(all_cand)
        """

        def find_height_diam(root):
            if root is None or (root.left is None and root.right is None):
                return (0, 0)
            
            add_factor = 0
            if root.left is not None:
                add_factor += 1
            
            if root.right is not None:
                add_factor += 1
            
            left_height, left_diam = find_height_diam(root.left)
            right_height, right_diam = find_height_diam(root.right)
            curr_cand = [left_diam, right_diam, left_height + right_height + add_factor]
            return (max(left_height, right_height) + 1, max(curr_cand))
        
        return find_height_diam(root)[1]

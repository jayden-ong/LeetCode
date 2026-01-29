# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        answer = [root, 0]
        # Returns the lowest depth of node found
        def find_smallest_subtree(root, curr_depth):
            if root.left is None and root.right is None:
                if curr_depth >= answer[1]:
                    answer[0], answer[1] = root, curr_depth
                return curr_depth
            
            left_depth = float('-inf')
            if root.left is not None:
                left_depth = find_smallest_subtree(root.left, curr_depth + 1)

            right_depth = float('-inf')
            if root.right is not None:
                right_depth = find_smallest_subtree(root.right, curr_depth + 1)
            
            if left_depth == right_depth and left_depth >= answer[1]:
                answer[0], answer[1] = root, left_depth
            return max(left_depth, right_depth)

        find_smallest_subtree(root, 0)
        return answer[0]
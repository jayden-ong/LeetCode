# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_largest_depth(root, curr_depth):
            if root.left is None and root.right is None:
                return curr_depth

            if root.left is None:
                return find_largest_depth(root.right, curr_depth + 1)
            
            if root.right is None:
                return find_largest_depth(root.left, curr_depth + 1)
            
            return max(find_largest_depth(root.right, curr_depth + 1), find_largest_depth(root.left, curr_depth + 1))
        max_depth = find_largest_depth(root, 0)
        def find_num_leaves(root, curr_depth):
            if curr_depth == max_depth:
                return 1
            
            answer = 0
            if root.left is not None:
                answer += find_num_leaves(root.left, curr_depth + 1)
            
            if root.right is not None:
                answer += find_num_leaves(root.right, curr_depth + 1)
            return answer
        num_leaves = find_num_leaves(root, 0)

        answer = [-1, None]
        def helper(root, curr_depth):
            # Must be a leaf
            if curr_depth == max_depth:
                if num_leaves == 1:
                    answer[0], answer[1] = curr_depth, root
                return 1
            
            num_lowest_leaves = 0
            if root.left is not None:
                num_lowest_leaves += helper(root.left, curr_depth + 1)
            
            if root.right is not None:
                num_lowest_leaves += helper(root.right, curr_depth + 1)
            
            if num_lowest_leaves == num_leaves:
                if curr_depth > answer[0]:
                    answer[0], answer[1] = curr_depth, root
            
            return num_lowest_leaves
            
        helper(root, 0)
        return answer[1]
        
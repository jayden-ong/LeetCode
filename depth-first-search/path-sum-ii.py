# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root, curr_sum, curr_vals):
            # Stop searching if current sum is greater than target sum
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                if curr_sum + root.val == targetSum:
                    return [curr_vals + [root.val]]
                else:
                    return []
            
            answer = []
            if root.left is not None:
                answer += helper(root.left, curr_sum + root.val, curr_vals + [root.val])
            if root.right is not None:
                answer += helper(root.right, curr_sum + root.val, curr_vals + [root.val])
            return answer

        return helper(root, 0, [])
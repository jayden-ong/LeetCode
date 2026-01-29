# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = pow(10, 9) + 7
        def get_sum(root):
            answer = root.val
            if root.left is not None:
                answer += get_sum(root.left)
            if root.right is not None:
                answer += get_sum(root.right)
            return answer
        
        tree_sum = get_sum(root)
        answer = [0]
        def split_tree(root):
            curr_sum = root.val
            if root.left is not None:
                curr_sum += split_tree(root.left)
            if root.right is not None:
                curr_sum += split_tree(root.right)
            
            answer[0] = max(answer[0], curr_sum * (tree_sum - curr_sum))
            return curr_sum

        split_tree(root)
        return answer[0] % MOD
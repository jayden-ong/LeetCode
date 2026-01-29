# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        def helper(curr_node, curr_depth):
            # Length of answer should always be 1 more than current depth
            if root is None:
                return
            
            if len(answer) < 1 + curr_depth:
                answer.append([curr_node.val])
            else:
                answer[curr_depth].append(curr_node.val)
            
            # Go left first
            if curr_node.left is not None:
                helper(curr_node.left, curr_depth + 1)
            
            if curr_node.right is not None:
                helper(curr_node.right, curr_depth + 1)
        
        helper(root, 0)
        return answer[::-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def recursive(curr_node, curr_depth):
            if curr_node is None:
                return
            
            if len(answer) < curr_depth + 1:
                answer.append(curr_node.val)
            
            if curr_node.right is not None:
                recursive(curr_node.right, curr_depth + 1)
            
            if curr_node.left is not None:
                recursive(curr_node.left, curr_depth + 1)

        recursive(root, 0)
        return answer
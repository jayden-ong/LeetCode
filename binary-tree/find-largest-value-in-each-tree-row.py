# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        answer = []
        def process_level(root, level):
            if level + 1 > len(answer):
                answer.append(root.val)
            else:
                answer[level] = max(answer[level], root.val)
            
            if root.left is not None:
                process_level(root.left, level + 1)
            if root.right is not None:
                process_level(root.right, level + 1)
        
        process_level(root, 0)
        return answer
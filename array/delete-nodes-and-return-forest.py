# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        answer = []
        def perform_delete(root, is_root):
            if root is None:
                return None
            
            if root.val in to_delete:
                root.left = perform_delete(root.left, True)
                root.right = perform_delete(root.right, True)
                return None
            else:
                root.left = perform_delete(root.left, False)
                root.right = perform_delete(root.right, False)
                if is_root:
                    answer.append(root)
                return root
        perform_delete(root, True)
        return answer
            
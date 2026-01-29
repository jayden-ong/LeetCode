# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None:
                return False
            elif root2 is None:
                return False
            else:
                return root1.val == root2.val and is_same(root1.left, root2.left) and is_same(root1.right, root2.right)

        if root is None:
            return False
        if root.left is None and root.right is None:
            return is_same(root, subRoot)
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
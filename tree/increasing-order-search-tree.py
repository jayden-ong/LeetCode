# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root
        elif root.left is None:
            right = self.increasingBST(root.right)
            root.right = right
            return root
        elif root.right is None:
            left = self.increasingBST(root.left)
            curr = left
            while curr.right is not None:
                curr = curr.right
            root.left = None
            curr.right = root
            return left
        else:
            left = self.increasingBST(root.left)
            right = self.increasingBST(root.right)
            #print(root.val)
            #print(left)
            #print(right)
            #print("---")
            root.left = None
            root.right = right
            curr = left
            while curr.right is not None:
                curr = curr.right
            curr.right = root
            return left
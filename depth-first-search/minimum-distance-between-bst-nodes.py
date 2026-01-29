# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None or (root.left is None and root.right is None):
            return float('inf')

        greatest_left = None
        curr = root.left
        if curr is not None:
            while curr.right is not None:
                curr = curr.right
            greatest_left = curr.val
        
        smallest_right = None
        curr = root.right
        if curr is not None:
            while curr.left is not None:
                curr = curr.left
            smallest_right = curr.val
        
        curr_smallest = float('inf')
        if greatest_left is not None:
            curr_smallest = min(root.val - greatest_left, curr_smallest)
        
        if smallest_right is not None:
            curr_smallest = min(smallest_right - root.val, curr_smallest)
        
        curr_smallest = min(self.minDiffInBST(root.left), curr_smallest)
        curr_smallest = min(self.minDiffInBST(root.right), curr_smallest)
        return curr_smallest
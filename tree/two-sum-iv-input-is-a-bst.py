# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def extract_elements(root):
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                return [root.val]
            
            return extract_elements(root.left) + [root.val] + extract_elements(root.right)
        
        if root.left is None and root.right is None:
            return False
        
        all_elements = extract_elements(root)
        num_elements = len(all_elements)
        i = 0
        j = num_elements - 1
        while i < j:
            if all_elements[i] + all_elements[j] == k:
                return True
            elif all_elements[i] + all_elements[j] < k:
                i += 1
            else:
                j -= 1
        return False
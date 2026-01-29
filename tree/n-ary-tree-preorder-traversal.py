"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        if root.children is None:
            return [root.val]

        res = [root.val]
        for child in root.children:
            if child is not None:
                res += self.preorder(child)
        return res
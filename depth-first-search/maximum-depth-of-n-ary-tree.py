"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        stack = [(0, root)]
        max_depth = 0
        while stack:
            curr_depth, curr_node = stack.pop()
            if curr_node.children is not None:
                # Assume children is a list
                for child in curr_node.children:
                    stack.append((curr_depth + 1, child))
            max_depth = max(max_depth, curr_depth)
        return max_depth + 1
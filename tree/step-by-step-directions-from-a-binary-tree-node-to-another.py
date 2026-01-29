# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Have to find the start first
        def find_start(root):
            if root.val == startValue:
                return (True, [(root, None)])
            
            if root.left is not None:
                status, result = find_start(root.left)
                result += [(root, "left")]
                if status:
                    return (True, result)
            
            if root.right is not None:
                status, result = find_start(root.right)
                result += [(root, "right")]
                if status:
                    return (True, result)
            
            return (False, [])
        
        _, path_from_root = find_start(root)
        '''
        for node, direction in path_from_root:
            print(node.val)
            print(direction)
        '''

        def find_destination(root):
            if root is None:
                return (False, "")
            
            if root.val == destValue:
                return (True, "")
            
            if root.left is not None:
                result, directions = find_destination(root.left)
                directions = "L" + directions
                if result:
                    return (True, directions)
            
            if root.right is not None:
                result, directions = find_destination(root.right)
                directions = "R" + directions
                if result:
                    return (True, directions)

            return (False, "")

        curr_path = ""
        for node, direction in path_from_root:
            #print(node.val)
            #print(direction)
            if node.val == destValue:
                return curr_path
            
            if direction is None:
                result, directions = find_destination(node)
            elif direction == "left":
                result, directions = find_destination(node.right)
            else:
                result, directions = find_destination(node.left)
            
            if result:
                if direction == "left":
                    return curr_path + "R" + directions
                elif direction == "right":
                    return curr_path + "L" + directions
                else:
                    return curr_path + directions
            curr_path += "U"
        # SHOULD NEVER RUN
        return ""
                
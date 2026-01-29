# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        nums_to_letters_dict = {0:"a",1:"b",2:"c",3:"d",
                                4:"e",5:"f",6:"g",7:"h",
                                8:"i",9:"j",10:"k",11:"l",
                                12:"m",13:"n",14:"o",15:"p",
                                16:"q",17:"r",18:"s",19:"t",
                                20:"u",21:"v",22:"w",23:"x",
                                24:"y",25:"z"}
        if root is None:
            return ""
        
        if root.left is None and root.right is None:
            return nums_to_letters_dict[root.val]
        
        def helper(root, curr):
            if root is None:
                return curr
            
            if root.left is None and root.right is None:
                return [root.val] + curr
            
            if root.right is None:
                return helper(root.left, [root.val] + curr)
            
            if root.left is None:
                return helper(root.right, [root.val] + curr)
            
            right_smallest = helper(root.right, [root.val] + curr)
            right_length = len(right_smallest)
            i = 0
            left_smallest = helper(root.left, [root.val] + curr)
            left_length = len(left_smallest)
            j = 0
            while i < right_length and j < left_length:
                if right_smallest[i] < left_smallest[j]:
                    return right_smallest
                elif left_smallest[j] < right_smallest[i]:
                    return left_smallest
                i += 1
                j += 1

            if i == right_length:
                return right_smallest
            return left_smallest
        
        best_answer = helper(root, [])
        curr_answer = ""
        for num in best_answer:
            curr_answer += nums_to_letters_dict[num]
        return curr_answer
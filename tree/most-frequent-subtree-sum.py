# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        answer_dict = {}
        def get_subtree_sum(root):
            if root.left is None and root.right is None:
                # For the leaf
                if root.val in answer_dict:
                    answer_dict[root.val] += 1
                else:
                    answer_dict[root.val] = 1
                return root.val
            
            curr_sum = root.val
            if root.left is not None:
                curr_sum += get_subtree_sum(root.left)
            
            if root.right is not None:
                curr_sum += get_subtree_sum(root.right)
            
            if curr_sum in answer_dict:
                answer_dict[curr_sum] += 1
            else:
                answer_dict[curr_sum] = 1
            return curr_sum
        
        get_subtree_sum(root)
        curr_max = float('-inf')
        answer = []
        for key in answer_dict:
            if answer_dict[key] > curr_max:
                curr_max = answer_dict[key]
                answer = [key]
            elif answer_dict[key] == curr_max:
                answer.append(key)
        return answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        num_nums = len(nums)
        if num_nums == 0:
            return None
        middle = num_nums // 2
        return TreeNode(nums[middle], self.sortedArrayToBST(nums[:middle]), self.sortedArrayToBST(nums[middle + 1:]))
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 1
        num_nums = len(nums)
        left = 0
        right = 0
        for j in range(1, num_nums):
            right += nums[j]
        
        if left == right:
            return 0
        
        while i < num_nums:
            left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
            i += 1

        return -1
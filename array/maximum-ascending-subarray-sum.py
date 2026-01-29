class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        num_nums = len(nums)
        streak = 0
        answer = 0
        if num_nums == 1:
            return nums[0]
        
        for i in range(1, num_nums):
            streak += nums[i - 1]
            if nums[i - 1] >= nums[i]:
                answer = max(answer, streak)
                streak = 0
        if nums[-2] < nums[-1]:
            streak += nums[-1]
        
        return max(answer, streak)
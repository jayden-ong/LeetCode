class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length_nums = len(nums)
        dp = [0] * length_nums
        answer = nums[0]
        for i in range(length_nums):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + max(0, dp[i - 1])
                answer = max(answer, dp[i])
        return answer
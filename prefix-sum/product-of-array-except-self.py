class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = []
        curr = 1
        dp.append(curr)
        for i in range(len(nums) - 1):
            curr *= nums[i]
            dp.append(curr)
        
        second_dp = []
        curr = 1
        second_dp.append(curr)
        for i in range(len(nums) - 1, 0, -1):
            curr *= nums[i]
            second_dp.append(curr)
        
        answer = []
        for i in range(len(nums)):
            answer.append(dp[i] * second_dp[len(nums) - i - 1])
        return answer
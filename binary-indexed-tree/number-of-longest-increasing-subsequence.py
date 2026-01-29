class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # First dp stores longest increasing subsequence
        # Second dp stores how many ways we can make longest increasing subsequence
        dp = [1] * len(nums)
        dp2 = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dp2[i] = dp2[j]
                    elif dp[j] + 1 == dp[i]:
                        dp2[i] += dp2[j]
        longest_inc_sub = max(dp)
        answer = 0
        for i in range(len(dp)):
            if dp[i] == longest_inc_sub:
                answer += dp2[i]
        return answer
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def most_money(houses):
            if len(houses) <= 2:
                return max(houses)
            dp = []
            dp.append(houses[0])
            dp.append(max(houses[0], houses[1]))
            for i in range(2, len(houses)):
                dp.append(max(dp[i - 2] + houses[i], dp[i - 1]))
            return dp[-1]
        
        return max(most_money(nums[1:]), most_money(nums[:-1]))
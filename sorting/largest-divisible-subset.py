class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[nums[0]]]
        answer = [nums[0]]
        for i in range(1, len(nums)):
            curr_best = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(curr_best) < len(dp[j]) + 1:
                    curr_best = dp[j] + [nums[i]]
            dp.append(curr_best)
            if len(curr_best) > len(answer):
                answer = curr_best
        #print(dp)
        return answer

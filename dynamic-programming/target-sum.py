class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        answer = 0

        dp = {}
        def choice(curr_index, curr_sum):
            if curr_index >= len(nums):
                if curr_sum == target:
                    return 1
                return 0
            
            if curr_index in dp and curr_sum in dp[curr_index]:
                return dp[curr_index][curr_sum]
            
            # Can either add or subtract
            answer = 0
            answer += choice(curr_index + 1, curr_sum + nums[curr_index])
            answer += choice(curr_index + 1, curr_sum - nums[curr_index])
            
            if curr_index not in dp:
                dp[curr_index] = {}

            dp[curr_index][curr_sum] = answer

            return answer

        return choice(0, 0)

        
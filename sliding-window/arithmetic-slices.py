class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # dp - at each index, store the number of arith subarrays
        if len(nums) < 3:
            return 0
        
        answer = 0
        curr_streak = 1
        curr_diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if curr_diff == nums[i] - nums[i - 1]:
                answer += curr_streak
                curr_streak += 1
            else:
                curr_diff = nums[i] - nums[i - 1]
                curr_streak = 1
        return answer
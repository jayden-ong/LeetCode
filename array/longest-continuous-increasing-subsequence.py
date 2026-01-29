class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # Once we find a pair of non-increasing values, have to start over
        curr_streak = 1
        max_streak = 1
        num_nums = len(nums)
        for i in range(1, num_nums):
            # Streak ended
            if nums[i - 1] >= nums[i]:
                max_streak = max(curr_streak, max_streak)
                curr_streak = 1
            else:
                curr_streak += 1
        return max(max_streak, curr_streak)
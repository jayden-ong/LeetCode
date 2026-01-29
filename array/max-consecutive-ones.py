class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_streak = 0
        max_streak = 0
        for num in nums:
            if num == 1:
                curr_streak += 1
            else:
                max_streak = max(curr_streak, max_streak)
                curr_streak = 0
        return max(max_streak, curr_streak)
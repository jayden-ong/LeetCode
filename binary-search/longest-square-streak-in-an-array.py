class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streak_dict = {}
        nums = sorted(nums, reverse=True)
        answer = 0
        for num in nums:
            if num * num in streak_dict:
                streak_dict[num] = streak_dict[num * num] + 1
            else:
                streak_dict[num] = 1
            answer = max(answer, streak_dict[num])
        
        if answer == 1:
            return -1
        return answer
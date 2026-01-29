class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        streak = 0
        k = max(nums)
        for num in nums:
            if num == k:
                streak += 1
            else:
                streak = 0
            answer = max(answer, streak)
        return answer
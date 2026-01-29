class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr_streak = 0
        answer = 0
        for num in nums:
            if num == 0:
                curr_streak += 1
                answer += curr_streak
            else:
                curr_streak = 0
        return answer
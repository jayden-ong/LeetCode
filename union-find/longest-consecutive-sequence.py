class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        answer = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr_streak = 0
                while num in nums_set:
                    num += 1
                    curr_streak += 1
                answer = max(curr_streak, answer)
        return answer
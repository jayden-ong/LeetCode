class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        streak = 0
        groups = []
        answer = 0
        for i, num in enumerate(nums):
            if num == 1:
                streak += 1
            else:
                groups.append(streak)
                streak = 0
            
            if i == len(nums) - 1 and streak > 0:
                groups.append(streak)
        
        # Everything is a 1
        if len(groups) == 1 and groups[0] == len(nums):
            return len(nums) - 1
        
        for i in range(len(groups) - 1):
            answer = max(answer, groups[i] + groups[i + 1])
        return answer
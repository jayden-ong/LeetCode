class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        starting_index = 0
        answer = 1
        curr = 1
        i = 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1
        
        if i == len(nums):
            return 1
        
        increasing = nums[i - 1] < nums[i]
        i += 1
        answer += 1
        curr += 1
        while i < len(nums):
            if (increasing and nums[i - 1] < nums[i]) or (not increasing and nums[i - 1] > nums[i]):
                curr += 1
            else:
                while i < len(nums) and nums[i - 1] == nums[i]:
                    i += 1
                
                if i < len(nums):
                    increasing = nums[i - 1] < nums[i]
                answer = max(answer, curr)
                curr = 2
            i += 1
        return max(answer, curr)
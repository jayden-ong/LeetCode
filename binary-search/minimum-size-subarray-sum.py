class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        curr_sum = 0
        answer = float('inf')
        while right < len(nums):
            curr_sum += nums[right]
            if curr_sum >= target:
                answer = min(answer, right - left + 1)
                while left <= right and curr_sum >= target:
                    curr_sum -= nums[left]
                    left += 1
                answer = min(answer, right - left + 2) 
            right += 1
        
        if answer == float('inf'):
            return 0
        return answer
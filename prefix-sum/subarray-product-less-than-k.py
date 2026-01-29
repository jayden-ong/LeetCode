class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left = 0
        right = 0
        curr_amount = 1
        answer = 0
        while right < len(nums):
            curr_amount *= nums[right]
            # Need to keep shrinking window until valid
            while curr_amount >= k:
                curr_amount //= nums[left]
                left += 1
            
            answer += right - left + 1
            right += 1
        return answer
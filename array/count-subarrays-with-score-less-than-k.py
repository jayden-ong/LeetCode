class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr = 0
        right = 0
        answer = 0
        for start in range(len(nums)):
            right = max(right, start)
            while right < len(nums) and curr * (right - start) < k:
                curr += nums[right]
                right += 1
            
            if right < len(nums):
                answer += right - start - 1
            elif right == len(nums):
                answer += right - start
                if curr * (right - start) >= k:
                    answer -= 1
                
            curr -= nums[start]
        return answer
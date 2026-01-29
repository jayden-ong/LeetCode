class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        curr = 0
        for num in nums:
            curr += num
            prefix_sum.append(curr)
        
        minimum_prefix = [float('inf')] * k
        minimum_prefix[0] = 0
        answer = float('-inf')
        curr = 0
        for i, num in enumerate(nums):
            curr += num
            mod = (i + 1) % k
            # We store the smallest prefix sum whose MOD matches the current one
            if minimum_prefix[mod] != float('inf'):
                answer = max(answer, curr - minimum_prefix[mod])
            
            minimum_prefix[mod] = min(minimum_prefix[mod], curr)
        return answer
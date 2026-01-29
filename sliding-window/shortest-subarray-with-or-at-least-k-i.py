class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = float('inf')
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr |= nums[j]
                if curr >= k:
                    answer = min(j - i + 1, answer)
        if answer == float('inf'):
            return -1
        return answer
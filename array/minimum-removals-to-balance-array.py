class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = float('inf')
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[i] * k >= nums[j]:
                j += 1
            answer = min(answer, len(nums) - (j - i))
        return answer
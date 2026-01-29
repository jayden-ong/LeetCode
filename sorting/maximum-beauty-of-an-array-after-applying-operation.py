class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        # Difference between two elements can be at most 2 * k
        left = 0
        right = 0
        answer = 0
        while right < len(nums):
            while right < len(nums) and nums[right] - nums[left] <= 2 * k:
                right += 1
                answer = max(answer, right - left)
            left += 1
            right += 1
        return answer
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_distance = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            max_distance = max(max_distance, abs(nums[i] - nums[i + 1]))
        return max_distance
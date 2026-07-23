class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        return len(nums) + 1
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        largest_num = max(nums)
        smallest_num = min(nums)
        if largest_num - smallest_num <= 2 * k:
            return 0
        else:
            return (largest_num - k) - (smallest_num + k)
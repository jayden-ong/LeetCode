class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 0
        lowest_point = start
        for num in nums:
            start += num
            lowest_point = min(lowest_point, start)
        
        return 1 - lowest_point
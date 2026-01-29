class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        heapq.heapify(nums)
        heapq.heappop(nums)
        return heapq.heappop(nums)
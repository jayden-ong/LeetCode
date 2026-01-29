class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        
        for i in range(k, len(nums)):
            num_to_insert = max(nums[i], heapq.heappop(heap))
            heapq.heappush(heap, num_to_insert)
        
        return heapq.heappop(heap)
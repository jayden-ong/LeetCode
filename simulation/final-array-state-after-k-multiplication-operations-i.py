class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_heap = []
        for index, val in enumerate(nums):
            heapq.heappush(nums_heap, (val, index))
        
        for i in range(k):
            val, index = heapq.heappop(nums_heap)
            heapq.heappush(nums_heap, (val * multiplier, index))
        
        answer = [0] * len(nums)
        while nums_heap:
            val, index = heapq.heappop(nums_heap)
            answer[index] = val
        return answer
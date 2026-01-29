class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_heap = []
        answer = 0
        for num in nums:
            if len(nums_heap) == 0:
                if num > 0:
                    heapq.heappush(nums_heap, -num)
                continue
            
            # Means we are increasing
            if -nums_heap[0] < num:
                heapq.heappush(nums_heap, -num)
            elif -nums_heap[0] > num:
                # We are decreasing and cannot chain any number that is larger
                while nums_heap and -nums_heap[0] > num:
                    heapq.heappop(nums_heap)
                    answer += 1
                
                if num != 0 and (len(nums_heap) == 0 or -nums_heap[0] < num):
                    heapq.heappush(nums_heap, -num)
        return answer + len(nums_heap)

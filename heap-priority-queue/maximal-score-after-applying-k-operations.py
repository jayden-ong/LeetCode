class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums_heap = []
        for num in nums:
            heapq.heappush(nums_heap, -num)
        
        answer = 0
        for i in range(k):
            curr_num = -1 * heapq.heappop(nums_heap)
            answer += curr_num
            if curr_num % 3 == 0:
                heapq.heappush(nums_heap, -1 * (curr_num // 3))
            else:
                temp = curr_num // 3
                temp += 1
                heapq.heappush(nums_heap, -1 * temp)
        return answer
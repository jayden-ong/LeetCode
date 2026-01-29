class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # The smallest num will always be nums[0]
        # The greatest num will be the sum of all elements

        # Brute force
        answer_heap = []
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                heapq.heappush(answer_heap, curr_sum)
        
        answer = 0
        curr_index = 0
        while curr_index < right:
            curr_num = heapq.heappop(answer_heap)
            if curr_index >= left - 1:
                answer += curr_num
            curr_index += 1
        
        return answer % (pow(10, 9) + 7)
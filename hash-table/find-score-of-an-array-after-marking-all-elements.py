class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums_heap = []
        for i in range(len(nums)):
            heapq.heappush(nums_heap, (nums[i], i))
        
        banned = set()
        answer = 0
        while nums_heap:
            curr_num, curr_index = heapq.heappop(nums_heap)
            while nums_heap and curr_index in banned:
                curr_num, curr_index = heapq.heappop(nums_heap)
            
            if curr_index in banned:
                return answer
            
            answer += curr_num
            banned.add(curr_index)
            banned.add(curr_index - 1)
            banned.add(curr_index + 1)
        return answer
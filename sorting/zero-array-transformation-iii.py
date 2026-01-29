class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int: 
        # Sort by start points       
        queries.sort(key=lambda x: x[0])
        curr = 0
        modifiers = [0] * len(nums)
        queries_index = 0
        queries_heap = []
        for i in range(len(nums)):
            while queries_index < len(queries) and queries[queries_index][0] == i:
                heapq.heappush(queries_heap, -queries[queries_index][1])
                queries_index += 1
            
            curr += modifiers[i]
            while nums[i] + curr > 0 and queries_heap and queries_heap[0] * -1 >= i:
                curr_right = -heapq.heappop(queries_heap)
                curr -= 1
                if curr_right + 1 < len(nums):
                    modifiers[curr_right + 1] += 1
            
            if nums[i] + curr > 0:
                return -1
            
        return len(queries_heap)
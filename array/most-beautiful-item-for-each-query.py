class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        answer = [0] * len(queries)
        new_queries = []
        for index, query in enumerate(queries):
            heapq.heappush(new_queries, (query, index))
        
        valid_items = []
        low_cost_items = []
        for price, beauty in items:
            heapq.heappush(low_cost_items, (price, beauty))
        
        while new_queries:
            # For each iteration, max_price will be non-decreasing
            max_price, curr_index = heapq.heappop(new_queries)
            # Top of the low_cost_items heap will be lowest cost item
            while low_cost_items and low_cost_items[0][0] <= max_price:
                price, beauty = heapq.heappop(low_cost_items)
                heapq.heappush(valid_items, -beauty)
            
            if valid_items:
                answer[curr_index] = valid_items[0] * -1
        return answer
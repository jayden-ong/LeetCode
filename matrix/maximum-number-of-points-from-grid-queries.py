class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0])
        
        answer = [0] * len(queries)
        queries_heap = []
        for i, query in enumerate(queries):
            heapq.heappush(queries_heap, (query, i))
        
        curr_score = 0
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while queries_heap:
            curr_query, curr_index = heapq.heappop(queries_heap)
            # Need to search by smallest
            while pq and pq[0][0] < curr_query:
                curr_tile, curr_row, curr_col = heapq.heappop(pq)
                curr_score += 1
                for add_row, add_col in directions:
                    new_row, new_col = add_row + curr_row, add_col + curr_col
                    if (new_row, new_col) not in visited and is_valid(new_row, new_col):
                        heapq.heappush(pq, (grid[new_row][new_col], new_row, new_col))
                        visited.add((new_row, new_col))
                
            
            answer[curr_index] = curr_score
        return answer
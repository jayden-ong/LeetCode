class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        heap = [(matrix[0][0], 0, 0)]
        visited = set()
        answer = None
        while k > 0:
            answer, curr_row, curr_col = heapq.heappop(heap)
            if curr_row < num_rows - 1 and (curr_row + 1, curr_col) not in visited:
                heapq.heappush(heap, (matrix[curr_row + 1][curr_col], curr_row + 1, curr_col))
                visited.add((curr_row + 1, curr_col))
            
            if curr_col < num_cols - 1 and (curr_row, curr_col + 1) not in visited:
                heapq.heappush(heap, (matrix[curr_row][curr_col + 1], curr_row, curr_col + 1))
                visited.add((curr_row, curr_col + 1))
            
            k -= 1
        return answer
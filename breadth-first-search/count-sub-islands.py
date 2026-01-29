from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def is_valid(i, j):
            return 0 <= i < len(grid1) and 0 <= j < len(grid1[0])

        def count_sub(grid, islands):
            answer = 0
            visited = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        queue = deque()
                        queue.append((i, j))
                        visited.add((i, j))
                        is_sub = True
                        if islands[i][j] == 0:
                            is_sub = False
                        
                        while queue:
                            curr_i, curr_j = queue.popleft()
                            for direction in directions:
                                new_i, new_j = curr_i + direction[0], curr_j + direction[1]
                                if is_valid(new_i, new_j) and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                                    visited.add((new_i, new_j))
                                    queue.append((new_i, new_j))
                                    if islands[new_i][new_j] == 0:
                                        is_sub = False
                        if is_sub:
                            answer += 1
            return answer
        return count_sub(grid2, grid1)
        
                                    
            
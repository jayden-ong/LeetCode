from collections import deque
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < m and 0 <= curr_col < n
        
        unexplored_cells = deque()
        # Contains all cells that are guarded
        guarded_cells = set()
        walls_set = set()
        for wall in walls:
            walls_set.add(tuple(wall))
        # Contains all directions and cells explored
        visited = set()

        for guard in guards:
            guard = tuple(guard)
            unexplored_cells.append(("", guard))
            guarded_cells.add(guard)
            visited.add(("up", guard))
            visited.add(("down", guard))
            visited.add(("right", guard))
            visited.add(("left", guard))

        while unexplored_cells:
            direction, coords = unexplored_cells.popleft()
            curr_row, curr_col = coords
            if (direction == "" or direction == "up") and is_valid(curr_row - 1, curr_col) and ("up", (curr_row - 1, curr_col)) not in visited and (curr_row - 1, curr_col) not in walls_set:
                visited.add(("up", (curr_row - 1, curr_col)))
                unexplored_cells.append(("up", (curr_row - 1, curr_col)))
                guarded_cells.add((curr_row - 1, curr_col))
            
            if (direction == "" or direction == "down") and is_valid(curr_row + 1, curr_col) and ("down", (curr_row + 1, curr_col)) not in visited and (curr_row + 1, curr_col) not in walls_set:
                visited.add(("down", (curr_row + 1, curr_col)))
                unexplored_cells.append(("down", (curr_row + 1, curr_col)))
                guarded_cells.add((curr_row + 1, curr_col))

            if (direction == "" or direction == "right") and is_valid(curr_row, curr_col + 1) and ("right", (curr_row, curr_col + 1)) not in visited and (curr_row, curr_col + 1) not in walls_set:
                visited.add(("right", (curr_row, curr_col + 1)))
                unexplored_cells.append(("right", (curr_row, curr_col + 1)))
                guarded_cells.add((curr_row, curr_col + 1))
            
            if (direction == "" or direction == "left") and is_valid(curr_row, curr_col - 1) and ("left", (curr_row, curr_col - 1)) not in visited and (curr_row, curr_col - 1) not in walls_set:
                visited.add(("left", (curr_row, curr_col - 1)))
                unexplored_cells.append(("left", (curr_row, curr_col - 1)))
                guarded_cells.add((curr_row, curr_col - 1))
            
        return m * n - len(guarded_cells) - len(walls_set)
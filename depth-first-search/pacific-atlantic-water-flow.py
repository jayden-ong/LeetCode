class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = set()
        num_rows = len(heights)
        num_cols = len(heights[0])
        heights_info = []
        stack = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def is_valid(i, j):
            return 0 <= i < num_rows and 0 <= j < num_cols
        # By default top right and bottom left corners can flow to both oceans
        # First index represents pacific
        for i in range(num_rows):
            new_row = []
            for j in range(num_cols):
                curr = []
                if i == 0 or j == 0:
                    stack.append((i, j, "pacific"))
                    visited.add((i, j, "pacific"))
                    curr.append(1)
                else:
                    curr.append(None)
                
                if i == num_rows - 1 or j == num_cols - 1:
                    stack.append((i, j, "atlantic"))
                    visited.add((i, j, "atlantic"))
                    curr.append(1)
                else:
                    curr.append(None)
                new_row.append(curr)
            heights_info.append(new_row)
        
        while stack:
            #print(stack)
            i, j, ocean = stack.pop()
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if is_valid(new_i, new_j) and heights[i][j] <= heights[new_i][new_j] and (new_i, new_j, ocean) not in visited:
                    if ocean == "pacific":
                        heights_info[new_i][new_j][0] = 1
                    if ocean == "atlantic":
                        heights_info[new_i][new_j][1] = 1
                    stack.append((new_i, new_j, ocean))
                    visited.add((new_i, new_j, ocean))
        print(heights_info)
        answer = []
        for i in range(num_rows):
            for j in range(num_cols):
                if heights_info[i][j][0] == 1 and heights_info[i][j][1] == 1:
                    answer.append([i, j])
        return answer
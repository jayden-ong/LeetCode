class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        num_rows = len(image)
        num_cols = len(image[0])
        searched = {}
        starting_color = image[sr][sc]
        while stack:
            # sr is row number and sc is col number
            curr_row, curr_col = stack.pop()
            if (curr_row, curr_col) not in searched:
                if curr_row > 0 and image[curr_row - 1][curr_col] == starting_color:
                    stack.append((curr_row - 1, curr_col))
                
                if curr_row < num_rows - 1 and image[curr_row + 1][curr_col] == starting_color:
                    stack.append((curr_row + 1, curr_col))
                
                if curr_col > 0 and image[curr_row][curr_col - 1] == starting_color:
                    stack.append((curr_row, curr_col - 1))
                
                if curr_col < num_cols - 1 and image[curr_row][curr_col + 1] == starting_color:
                    stack.append((curr_row, curr_col + 1))
                
                image[curr_row][curr_col] = color
                searched[(curr_row, curr_col)] = True
        return image
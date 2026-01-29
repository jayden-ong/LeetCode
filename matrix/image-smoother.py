class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1), (0, 0)]
        # Main idea is that we are looking at the cells around each one
        num_rows = len(img)
        num_cols = len(img[0])
        def is_valid(curr_row, curr_col):
            return 0 <= curr_row < num_rows and 0 <= curr_col < num_cols

        new_matrix = []
        for i in range(num_rows):
            new_row = []
            for j in range(num_cols):
                # Want to make sure we can look up
                curr_sum = 0
                num_added = 0
                for direction in directions:
                    new_row_val, new_col_val = i + direction[0], j + direction[1]
                    if is_valid(new_row_val, new_col_val):
                        curr_sum += img[new_row_val][new_col_val]
                        num_added += 1
                new_row.append(curr_sum // num_added)
            new_matrix.append(new_row)
        return new_matrix
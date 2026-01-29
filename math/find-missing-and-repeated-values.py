class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        curr_sum = 0
        seen_set = set()
        num_rows, num_cols = len(grid), len(grid)
        required_sum = 0
        first_answer = None
        for i in range(num_rows):
            for j in range(num_cols):
                curr_sum += grid[i][j]
                if grid[i][j] in seen_set:
                    first_answer = grid[i][j]
                else:
                    seen_set.add(grid[i][j])
                required_sum += i * num_cols + (j + 1)
        curr_sum -= first_answer
        second_answer = required_sum - curr_sum
        return [first_answer, second_answer]
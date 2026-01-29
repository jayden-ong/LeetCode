class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def get_first_second_min(nums, num_nums):
            first_min = None
            second_min = None
            first_min_index = -1
            second_min_index = -1
            for i in range(num_nums):
                if first_min is None:
                    first_min = nums[i]
                    first_min_index = i
                elif first_min is not None and second_min is None:
                    if nums[i] < first_min:
                        second_min = first_min
                        second_min_index = first_min_index
                        first_min = nums[i]
                        first_min_index = i
                    else:
                        second_min = nums[i]
                        second_min_index = i
                else:
                    if nums[i] < first_min:
                        second_min = first_min
                        second_min_index = first_min_index
                        first_min = nums[i]
                        first_min_index = i
                    elif nums[i] < second_min:
                        second_min = nums[i]
                        second_min_index = i
            return (first_min, first_min_index, second_min, second_min_index)

        num_rows = len(grid)
        num_cols = len(grid[0])
        dp = []
        for i in range(num_rows):
            if i == 0:
                dp.append(grid[i])
                first_min, first_min_index, second_min, second_min_index = get_first_second_min(grid[i], num_cols)
            # If there are two rows, get the min of both rows
            # If they are in the same column, there are two options:
            # Get the min of the first row and second min of the second row
            # Or get the second min of the second row and min of the first row
            else:
                curr_row = []
                for j in range(num_cols):
                    # Cannot choose the absolute min, go to next
                    if first_min_index == j:
                        curr_row.append(second_min + grid[i][j])
                    else:
                        curr_row.append(first_min + grid[i][j])
                first_min, first_min_index, second_min, second_min_index = get_first_second_min(curr_row, num_cols)
                dp.append(curr_row)
        return first_min
                
                
                
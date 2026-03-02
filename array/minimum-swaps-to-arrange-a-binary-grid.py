class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Need to find a row that has n - 1 0's at the end, n - 2 0's at the end, and so on.
        # It doesn't matter what the last row is, so we can ignore index 0 of "rows_needed"
        # Want to map each row number to where each row currently is
        desired_row_to_row = {}
        rows_complete = 0
        extra_row_index = None
        list_to_sort = []
        for i, row in enumerate(grid):
            num_zeros = 0
            for num in row:
                if num == 0:
                    num_zeros += 1
                else:
                    num_zeros = 0
            
            if len(grid) - num_zeros - 1 not in desired_row_to_row:
                rows_complete += 1
                desired_row_to_row[len(grid) - num_zeros - 1] = num_zeros
                list_to_sort.append(num_zeros)
            else:
                extra_row_index = i
                list_to_sort.append(0)

        # print(rows_needed)
        if rows_complete < len(grid) - 1:
            return -1
        
        # There are two possibilities for the bottom row
        #   There is a row with 0 0s above the diagonal -- it becomes the last row
        #   There are two rows with the same number of zeros -- the larger row becomes the last row
        # print(desired_row_to_row)
        answer = 0
        # Sort in descending order
        # print(list_to_sort)
        for i in range(len(grid) - 1, -1, -1):
            for j in range(i):
                if list_to_sort[j] < list_to_sort[j + 1]:
                    answer += 1
                    list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
            # print(list_to_sort)
        return answer
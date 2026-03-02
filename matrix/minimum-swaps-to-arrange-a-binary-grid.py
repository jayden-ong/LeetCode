class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Need to find a row that has n - 1 0's at the end, n - 2 0's at the end, and so on.
        # It doesn't matter what the last row is, so we can ignore index 0 of "rows_needed"
        # Want to map each row number to where each row currently is
        list_to_sort = []
        for i, row in enumerate(grid):
            num_zeros = 0
            for num in row:
                if num == 0:
                    num_zeros += 1
                else:
                    num_zeros = 0
            
            list_to_sort.append(num_zeros)
        
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
        
        for i, num in enumerate(list_to_sort):
            if num < len(grid) - i - 1:
                return -1
        return answer
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maximum_row = 0
        max_ones = mat[0].count(1)
        for i in range(1, len(mat)):
            num_ones = mat[i].count(1)
            if num_ones > max_ones:
                max_ones = num_ones
                maximum_row = i

        return [maximum_row, max_ones]
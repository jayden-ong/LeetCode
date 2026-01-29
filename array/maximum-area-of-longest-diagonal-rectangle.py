class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest_diagonal = 0
        answer = 0
        for dimension in dimensions:
            diagonal_length = pow(pow(dimension[0], 2) + pow(dimension[1], 2), 0.5)
            if diagonal_length > longest_diagonal or (diagonal_length == longest_diagonal and dimension[0] * dimension[1] > answer):
                answer = dimension[0] * dimension[1]
                longest_diagonal = diagonal_length
        return answer
                
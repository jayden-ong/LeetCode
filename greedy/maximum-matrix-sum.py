class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # If there is an even amount of negative numbers, answer is sum of all elements (make negative positive)
        # Otherwise, it is the sum of all elements with the minimum element in the entire matrix being negative
        num_negative = 0
        answer = 0
        smallest_num = float('inf')
        for row in matrix:
            for num in row:
                if num < 0:
                    num_negative += 1
                    answer -= num
                else:
                    answer += num
                smallest_num = min(smallest_num, abs(num))
        
        if num_negative % 2 == 0:
            return answer
        return answer - 2 * smallest_num
class Solution:
    def pivotInteger(self, n: int) -> int:
        curr_sum = 0
        for i in range(1, n + 1):
            curr_sum += i
        
        left_sum = 0
        for i in range(1, n + 1):
            left_sum += i
            if curr_sum == left_sum:
                return i
            curr_sum -= i
        return -1
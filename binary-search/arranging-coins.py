class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr_row = 0
        while n > 0:
            n = n - curr_row - 1
            curr_row += 1
        
        if n == 0:
            return curr_row
        return curr_row - 1
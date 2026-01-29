class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        curr_res = 1
        while curr_res < n:
            curr_res *= 3
        return curr_res == n
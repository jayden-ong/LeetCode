class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # When you get rid of the leftmost bit, you will always have something like 01.....0
        if n == 0:
            return 0
        
        k = 0
        curr = 1
        while 2 * curr <= n:
            curr *= 2
            k += 1
        
        return pow(2, k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)
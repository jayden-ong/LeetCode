class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1 or n == 81 or n == 225:
            return False
    
        if (n % 2 == 1 or n == 4) and pow(int(pow(n, 0.5)), 2) == n:
            return True
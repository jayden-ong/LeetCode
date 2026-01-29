class Solution:
    def integerBreak(self, n: int) -> int:
        # 2 - 1 * 1
        # 3 - 2 * 1
        # 4 - 2 * 2
        # 5 - 2 * 3
        # 6 - 3 * 3
        # 7 - 2 * 2 * 3
        # 8 - 2 * 3 * 3
        # 9 - 3 * 3 * 3
        # 10 - 3 * 3 * 2 * 2
        # 11 - 3 * 3 * 3 * 2
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        answer = 1
        while n > 4:
            answer *= 3
            n -= 3
        return answer * n

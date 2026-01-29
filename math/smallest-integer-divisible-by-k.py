class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        modulo = 0
        for answer in range(1, k + 1):
            modulo = (modulo * 10 + 1) % k
            if modulo == 0:
                return answer
        return -1
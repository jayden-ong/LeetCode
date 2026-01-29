class Solution:
    def smallestNumber(self, n: int) -> int:
        curr = 1
        while curr - 1 < n:
            curr *= 2
        return curr - 1
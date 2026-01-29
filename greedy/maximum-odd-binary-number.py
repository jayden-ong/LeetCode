class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_zero = 0
        num_one = 0
        for char in s:
            if char == "0":
                num_zero += 1
            else:
                num_one += 1
        
        return (max(num_one - 1, 0) * "1") + (num_zero * "0") + "1"
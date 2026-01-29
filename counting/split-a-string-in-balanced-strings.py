class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_substrings = 0
        num_R = 0
        num_L = 0
        for char in s:
            if char == "R":
                num_R += 1
            else:
                num_L += 1
            
            if num_L == num_R:
                num_substrings += 1
                num_R = 0
                num_L = 0
        return num_substrings
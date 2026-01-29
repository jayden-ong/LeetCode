class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        string_n = str(bin(n))
        for i in range(len(string_n)):
            if string_n[i] == "1":
                num += 1
        
        return num
        
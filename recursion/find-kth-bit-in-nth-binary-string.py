class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(binary_string):
            answer = ""
            for bit in binary_string:
                if bit == "0":
                    answer += "1"
                else:
                    answer += "0"
            return answer
        
        curr = "0"
        for i in range(n):
            inversion = invert(curr)
            curr = curr + "1" + inversion[::-1]
        return curr[k - 1]
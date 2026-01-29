class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i = 0
        binary_x = format(x, 'b')[::-1]
        j = 0
        binary_back_n = format(n - 1, 'b')[::-1]
        answer = ""
        while i < len(binary_x) or j < len(binary_back_n):
            if i >= len(binary_x):
                answer += binary_back_n[j]
                j += 1
            elif j >= len(binary_back_n):
                answer += binary_x[i]
                i += 1
            else:
                if binary_x[i] == "0":
                    answer += binary_back_n[j]
                    j += 1
                else:
                    answer += "1"
                i += 1
        return int(answer[::-1], 2)
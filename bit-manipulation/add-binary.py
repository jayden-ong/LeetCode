class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        length_a = len(a)
        length_b = len(b)
        i = length_a - 1
        j = length_b - 1
        answer = ""
        while i > -1 or j > -1:
            if i == -1:
                # Max 2
                if carry_over + int(b[j]) > 1:
                    answer = "0" + answer
                    carry_over = 1
                # 1 or less
                else:
                    answer = str(carry_over + int(b[j])) + answer
                    carry_over = 0  
                j -= 1
            elif j == -1:
                # Max 2
                if carry_over + int(a[i]) > 1:
                    answer = "0" + answer
                    carry_over = 1
                # 1 or less
                else:
                    answer = str(carry_over + int(a[i])) + answer
                    carry_over = 0
                i -= 1
            else:
                num = carry_over + int(a[i]) + int(b[j])
                # There is carryover and num is 2 or 3
                if num > 1:
                    answer = str(num % 2) + answer
                    carry_over = 1
                else:
                    answer = str(num) + answer
                    carry_over = 0
                i -= 1
                j -= 1
        
        if carry_over > 0:
            return "1" + answer
        return answer
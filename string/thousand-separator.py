class Solution:
    def thousandSeparator(self, n: int) -> str:
        string_n = str(n)
        length_n = len(string_n)
        if length_n < 4:
            return string_n
        
        answer = ""
        temp = 0
        for i in range(length_n - 1, -1, -1):
            temp += 1
            answer += string_n[i]
            if temp % 3 == 0 and i != 0:
                answer += '.'
                temp = 0

        return answer[::-1]
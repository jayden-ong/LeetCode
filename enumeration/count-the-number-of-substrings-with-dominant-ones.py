class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        answer = 0
        for i in range(len(s)):
            num_ones = 0
            num_zeros = 0
            for j in range(i, -1, -1):
                if s[j] == "1":
                    num_ones += 1
                else:
                    num_zeros += 1
                
                if num_ones >= pow(num_zeros, 2):
                    answer += 1
        return answer
        '''
        last_zero = [-1] * (len(s) + 1)
        for i in range(len(s)):
            if i == 0 or s[i - 1] == "0":
                last_zero[i + 1] = i
            else:
                last_zero[i + 1] = last_zero[i]
        
        answer = 0
        for i in range(1, len(s) + 1):
            num_zeros = 0
            if s[i - 1] == "0":
                num_zeros += 1 
            j = i
            while j > 0 and num_zeros ** 2 <= len(s):
                num_ones = (i - last_zero[j]) - num_zeros
                if num_zeros ** 2 <= num_ones:
                    answer += min(j - last_zero[j], num_ones - num_zeros ** 2 + 1)
                j = last_zero[j]
                num_zeros += 1
        return answer
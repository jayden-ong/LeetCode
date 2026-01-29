class Solution:
    def numSub(self, s: str) -> int:
        MOD = pow(10, 9) + 7
        answer = 0
        curr_length = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == "0":
                answer = (answer + (curr_length * (curr_length + 1)) // 2) % MOD
                curr_length = 0
            else:
                curr_length += 1
        return answer
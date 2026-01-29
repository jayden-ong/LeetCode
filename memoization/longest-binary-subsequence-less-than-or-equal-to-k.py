class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # It is optimal to start with all zeros
        curr_val = 0
        answer = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                answer += 1
            else:
                if curr_val + 2 ** answer <= k:
                    curr_val += 2 ** answer
                    answer += 1
        return answer
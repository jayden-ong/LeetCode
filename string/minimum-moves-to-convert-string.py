class Solution:
    def minimumMoves(self, s: str) -> int:
        length_s = len(s)
        answer = 0
        i = 0
        while i < length_s:
            if s[i] == "X":
                answer += 1
                i += 3
            else:
                i += 1
        return answer
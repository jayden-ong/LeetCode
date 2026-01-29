class Solution:
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                answer += 1
        return answer
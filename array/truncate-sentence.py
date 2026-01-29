class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        answer = ""
        for i in range(k):
            answer += s[i] + " "
        return answer.rstrip()
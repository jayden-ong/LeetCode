class Solution:
    def processStr(self, s: str, k: int) -> str:
        answer = ""
        for char in s:
            if char == "*":
                answer = answer[:-1]
            elif char == "#":
                answer = answer + answer
            elif char == "%":
                answer = answer[::-1]
            else:
                answer += char
        if k >= len(answer):
            return '.'
        return answer[k]
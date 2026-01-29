class Solution:
    def finalString(self, s: str) -> str:
        answer = ""
        for char in s:
            if char == "i":
                answer = answer[::-1]
            else:
                answer += char
        return answer
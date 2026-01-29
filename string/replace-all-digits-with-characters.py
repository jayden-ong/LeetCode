class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        for char in s:
            if char.isnumeric():
                answer += chr(ord(prev) + int(char))
            else:
                answer += char
            prev = char
        return answer
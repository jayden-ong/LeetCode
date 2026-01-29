class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        spaces_index = 0
        for i in range(len(s)):
            if spaces_index < len(spaces) and i == spaces[spaces_index]:
                answer += " "
                spaces_index += 1
            answer += s[i]
        return answer
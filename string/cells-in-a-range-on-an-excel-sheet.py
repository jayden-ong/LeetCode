class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1 = s[0]
        row1 = int(s[1])
        col2 = s[3]
        row2 = int(s[4])
        answer = []
        while ord(col1) <= ord(col2):
            for i in range(row1, row2 + 1):
                answer.append(col1 + str(i))
            col1 = chr(ord(col1) + 1)
        return answer
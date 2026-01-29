class Solution:
    def countAsterisks(self, s: str) -> int:
        bars_seen = 0
        answer = 0
        for char in s:
            if char == "|":
                bars_seen += 1
            else:
                if bars_seen % 2 == 0 and char == "*":
                    answer += 1
        return answer
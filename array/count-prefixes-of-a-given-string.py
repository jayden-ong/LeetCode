class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        answer = 0
        for word in words:
            if s[:len(word)] == word:
                answer += 1
        return answer

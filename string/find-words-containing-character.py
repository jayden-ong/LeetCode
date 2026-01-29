class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        i = 0
        for word in words:
            if x in word:
                answer.append(i)
            i += 1
        return answer
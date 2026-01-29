class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            answer = max(answer, len(sentence.split(' ')))
        return answer
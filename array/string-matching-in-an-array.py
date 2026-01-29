class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        num_words = len(words)
        answer = []
        for i in range(num_words):
            for j in range(num_words):
                if i != j and words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer
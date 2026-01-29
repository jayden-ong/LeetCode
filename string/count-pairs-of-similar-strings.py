class Solution:
    def similarPairs(self, words: List[str]) -> int:
        num_words = len(words)
        words_sets = []
        for i in range(num_words):
            word_set = set()
            for char in words[i]:
                word_set.add(char)
            words_sets.append(word_set)
        
        answer = 0
        for i in range(num_words - 1):
            for j in range(i + 1, num_words):
                if words_sets[i] == words_sets[j]:
                    answer += 1
        return answer
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        words_freq = {}
        for word in words:
            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1
        
        answer = 0
        for word in words_freq:
            word_index = 0
            for i in range(len(s)):
                if word[word_index] == s[i]:
                    word_index += 1
                    if word_index >= len(word):
                        answer += words_freq[word]
                        break
        return answer
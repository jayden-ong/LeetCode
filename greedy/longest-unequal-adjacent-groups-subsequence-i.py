class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        num_words = len(words)
        answer = [words[0]]
        prev_bit = groups[0]
        for i in range(1, num_words):
            if groups[i] != prev_bit:
                answer.append(words[i])
                prev_bit = groups[i]
        return answer
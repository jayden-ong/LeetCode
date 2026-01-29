class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words) - 1):
            curr_pre_suf = words[i]
            word_length = len(words[i])
            for j in range(i + 1, len(words)):
                curr_word = words[j]
                if curr_pre_suf == curr_word[:word_length] and curr_pre_suf == curr_word[len(curr_word) - word_length:]:
                    answer += 1
        return answer
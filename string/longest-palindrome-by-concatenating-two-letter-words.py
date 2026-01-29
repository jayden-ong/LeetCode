class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        answer = 0
        num_same = 0
        words_set = defaultdict(int)
        for word in words:
            if word[0] == word[1]:
                num_same += 1
            
            if words_set[word[1] + word[0]] > 0:
                answer += 4
                words_set[word[1] + word[0]] -= 1
                if word[0] == word[1]:
                    num_same -= 2
            else:
                words_set[word] += 1
            
        if num_same > 0:
            answer += 2
        return answer
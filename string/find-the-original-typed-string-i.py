class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        curr_length = 0
        for i in range(len(word) + 1):
            if i == len(word) or word[i] != word[i - 1]:
                if curr_length > 1:
                    answer += curr_length - 1
                curr_length = 1
            else:
                curr_length += 1
        return answer
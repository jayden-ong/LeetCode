class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        letters_dict = {}
        answer = -1
        length_s = len(s)
        for i in range(length_s):
            if s[i] in letters_dict:
                answer = max(answer, i - letters_dict[s[i]] - 1)
            else:
                letters_dict[s[i]] = i
        return answer
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        length1 = len(word1)
        length2 = len(word2)
        answer = ""
        while i < length1 and j < length2:
            answer += word1[i] + word2[j]
            i += 1
            j += 1

        if i == length1 and j != length2:
            answer += word2[j:]
        elif j == length2 and i != length1:
            answer += word1[i:]
        return answer
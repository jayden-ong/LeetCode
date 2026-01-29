class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters_set = set()
        answer = 0
        for char in word:
            if char.isupper():
                if char.lower() in letters_set and char not in letters_set:
                    answer += 1
            else:
                if char.upper() in letters_set and char not in letters_set:
                    answer += 1
            letters_set.add(char)
        return answer
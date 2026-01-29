class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set()
        for letter in brokenLetters:
            broken_set.add(letter)

        answer = 0
        words_list = text.split(' ')
        for word in words_list:
            broken = False
            for char in word:
                if char in broken_set:
                    broken = True
                    break
            if not broken:
                answer += 1
        return answer
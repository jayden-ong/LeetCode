class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        answer = 0
        letters_set = set()
        for letter in sentence:
            if letter in letters_set:
                continue
            else:
                letters_set.add(letter)
                answer += 1
        return answer == 26
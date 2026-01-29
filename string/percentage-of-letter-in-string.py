class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        answer = 0
        num_letters = 0
        for char in s:
            if char == letter:
                answer += 1
            num_letters += 1
        return int((answer * 100)/num_letters)
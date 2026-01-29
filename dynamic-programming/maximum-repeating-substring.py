class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        length_sequence = len(sequence)
        length_word = len(word)
        max_repetitions = length_sequence // length_word
        for i in range(max_repetitions, 0, -1):
            if word * i in sequence:
                return i
        return 0
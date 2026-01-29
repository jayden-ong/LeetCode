class Solution:
    def oddString(self, words: List[str]) -> str:
        length_word = len(words[0])
        length_words = len(words)
        for i in range(1, length_word):
            # Check first three words
            first_diff = ord(words[0][i]) - ord(words[0][i - 1])
            second_diff = ord(words[1][i]) - ord(words[1][i - 1])
            third_diff = ord(words[2][i]) - ord(words[2][i - 1])
            
            if first_diff == second_diff and first_diff == third_diff:
                required_diff = first_diff
                for j in range(3, length_words):
                    if ord(words[j][i]) - ord(words[j][i - 1]) != required_diff:
                        return words[j]
            else:
                if first_diff != second_diff and first_diff == third_diff:
                    return words[1]
                elif first_diff != second_diff and first_diff != third_diff:
                    return words[0]
                elif first_diff == second_diff and first_diff != third_diff:
                    return words[2]
                
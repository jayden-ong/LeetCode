class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Longer words come after shorter words
        order_dict = {}
        i = 0
        for char in order:
            order_dict[char] = i
            i += 1
        num_words = len(words)
        for j in range(1, num_words):
            word1_length = len(words[j - 1])
            word2_length = len(words[j])
            word1_pointer = 0
            word2_pointer = 0
            equal = True
            while word1_pointer < word1_length and word2_pointer < word2_length:
                if order_dict[words[j - 1][word1_pointer]] > order_dict[words[j][word2_pointer]]:
                    return False
                elif order_dict[words[j - 1][word1_pointer]] < order_dict[words[j][word2_pointer]]:
                    equal = False
                    break
                word1_pointer += 1
                word2_pointer += 1
            # All the characters matched (so far), but word1 is done, means word2 is shorter and comes before word 1
            if equal and word1_pointer != word1_length:
                return False
        return True
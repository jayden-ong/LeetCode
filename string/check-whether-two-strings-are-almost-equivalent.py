class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_dict = {}
        word2_dict = {}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            word1_dict[char] = 0
            word2_dict[char] = 0
        
        for letter in word1:
            word1_dict[letter] += 1
        
        for letter in word2:
            word2_dict[letter] += 1
        
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if abs(word1_dict[char] - word2_dict[char]) > 3:
                return False
        return True
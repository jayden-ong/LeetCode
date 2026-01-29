class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        num_words = len(words)
        letters_dict = {}
        for word in words:
            for char in word:
                if char in letters_dict:
                    letters_dict[char] += 1
                else:
                    letters_dict[char] = 1
        
        for key in letters_dict:
            if letters_dict[key] % num_words != 0:
                return False
        return True
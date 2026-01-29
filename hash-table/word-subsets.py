class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Want to collect all of the letters that have to appear in the the words of words1 for it to be uni.
        required_letters = defaultdict(int)
        for word in words2:
            letter_word = defaultdict(int)
            for letter in word:
                letter_word[letter] += 1
                required_letters[letter] = max(required_letters[letter], letter_word[letter])

        answer = []
        for word in words1:
            letters_dict = defaultdict(int)
            for letter in word:
                letters_dict[letter] += 1
            
            valid = True
            for letter in required_letters:
                if required_letters[letter] > letters_dict[letter]:
                    valid = False
                    break
                
            if valid:
                answer.append(word)

        return answer

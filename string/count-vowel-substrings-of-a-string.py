class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        answer = 0
        length_word = len(word)
        if length_word < 5:
            return 0
        
        for i in range(length_word - 4):
            vowel_set = set()
            num_vowels = 0
            unique_vowels = 0
            for j in range(i, length_word):
                if word[j] in 'aeiou':
                    if word[j] not in vowel_set:
                        vowel_set.add(word[j])
                        unique_vowels += 1
                    
                    if unique_vowels >= 5:
                        answer += 1
                else:
                    break
        return answer
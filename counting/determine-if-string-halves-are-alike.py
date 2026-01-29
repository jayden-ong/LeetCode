class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length_s = len(s)
        num_vowels_left = 0
        num_vowels_right = 0
        for i in range(length_s // 2):
            if s[i] in 'aeiouAEIOU':
                num_vowels_left += 1
        
        for j in range((length_s // 2), length_s):
            if s[j] in 'aeiouAEIOU':
                num_vowels_right += 1
        
        return num_vowels_left == num_vowels_right
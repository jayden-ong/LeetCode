class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowel = 0
        max_cons = 0
        chars_dict = defaultdict(int)
        for char in s:
            chars_dict[char] += 1
            if char in "aeiou":
                max_vowel = max(max_vowel, chars_dict[char])
            else:
                max_cons = max(max_cons, chars_dict[char])
        return max_vowel + max_cons
                
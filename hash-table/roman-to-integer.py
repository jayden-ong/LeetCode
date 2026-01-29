class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        curr_sum = 0
        for i in range(0, len(s)):
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                curr_sum -= roman_dict[s[i]]
            else:
                curr_sum += roman_dict[s[i]]
        
        return curr_sum
        
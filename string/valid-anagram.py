class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = { "a" : 0, "b" : 0, "c" : 0, "d" : 0,
                      "e" : 0, "f" : 0, "g" : 0, "h" : 0,
                      "i" : 0, "j" : 0, "k" : 0, "l" : 0,
                      "m" : 0, "n" : 0, "o" : 0, "p" : 0,
                      "q" : 0, "r" : 0, "s" : 0, "t" : 0,
                      "u" : 0, "v" : 0, "w" : 0, "x" : 0,
                      "y" : 0, "z" : 0}

        num_char_s = 0
        for char in s:
            char_dict[char] += 1
            num_char_s += 1
        
        num_char_t = 0
        for char in t:
            char_dict[char] -= 1
            if char_dict[char] < 0:
                return False
            num_char_t += 1
        
        return num_char_s == num_char_t
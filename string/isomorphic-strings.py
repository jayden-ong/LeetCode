class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        
        letters_dict = {}
        for i in range(length_s):
            if letters_dict.get(s[i], -1) == -1:
                letters_dict[s[i]] = t[i] 
            elif letters_dict[s[i]] != t[i]:
                return False
            
        letters_dict = {}
        for i in range(length_t):
            if letters_dict.get(t[i], -1) == -1:
                letters_dict[t[i]] = s[i] 
            elif letters_dict[t[i]] != s[i]:
                return False
        return True
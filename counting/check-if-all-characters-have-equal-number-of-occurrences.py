class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occur_dict = {}
        for char in s:
            if char in occur_dict:
                occur_dict[char] += 1
            else:
                occur_dict[char] = 1
        
        desired_occur = occur_dict[s[0]]
        for key in occur_dict:
            if occur_dict[key] != desired_occur:
                return False
        return True
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        
        if str1 == str2:
            return True
        
        conversion_dict = {'a' : 'b', 'b' : 'c', 'c' : 'd', 'd' : 'e', 'e' : 'f', 'f' : 'g', 'g' : 'h', 'h' : 'i', 'i' : 'j', 'j' : 'k', 'k' : 'l', 'l' : 'm', 'm' : 'n', 'n' : 'o', 'o' : 'p', 'p' : 'q', 'q' : 'r', 'r' : 's', 's' : 't', 't' : 'u', 'u' : 'v', 'v' : 'w', 'w' : 'x', 'x' : 'y', 'y' : 'z', 'z' : 'a'}
        converted_str1 = ""
        for char in str1:
            converted_str1 += conversion_dict[char]
        
        str2_index = 0
        for i in range(len(str1)):
            if str2[str2_index] == str1[i] or str2[str2_index] == converted_str1[i]:
                str2_index += 1
            
            if str2_index >= len(str2):
                return True
        return False
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        new_string = ""
        counter = 0
        string_length = len(s)
        for i in range(string_length - 1, -1, -1):
            # Want to increment counter to 1
            if s[i] == ')':
                counter += 1
            elif s[i] == '(':
                counter -= 1
            
            # There is a ( with no way to pair it with )
            if counter >= 0:
                new_string = s[i] + new_string
            else:
                counter += 1
        
        return new_string.replace(")", "", counter)
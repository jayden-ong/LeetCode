class Solution:
    def findLatestTime(self, s: str) -> str:
        new_string = ""
        if s[0] == "?":
            if s[1] == "?" or int(s[1]) < 2:
                new_string += "1"
            else:
                new_string += "0"
        else:
            new_string += s[0]
        
        if s[1] == "?":
            if new_string[0] == "1":
                new_string += "1"
            else:
                new_string += "9"
        else:
            new_string += s[1]
        
        new_string += ":"
        if s[3] == "?":
            new_string += "5"
        else:
            new_string += s[3]
        
        if s[4] == "?":
            new_string += "9"
        else:
            new_string += s[4]
        return new_string
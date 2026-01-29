class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
            return 0
        new_list = s.split(" ")
        num = 0
        for char in new_list:
            if char != "":
                num += 1
        
        return num
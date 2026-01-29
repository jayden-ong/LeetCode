class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            string_num = str(num)
            num = 0
            for char in string_num:
                num += int(char)
            
        return num
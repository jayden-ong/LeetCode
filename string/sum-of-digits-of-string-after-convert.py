class Solution:
    def getLucky(self, s: str, k: int) -> int:
        initial_string = ""
        for char in s:
            initial_string += str(ord(char) - 96)
        
        for i in range(k):
            temp = 0
            for char in initial_string:
                temp += int(char)
            initial_string = str(temp)
        return int(initial_string)
                
         
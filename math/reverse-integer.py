class Solution:
    def reverse(self, x: int) -> int:
        string_int = str(x)
        negative = False
        string_length = len(string_int)
        string_int = string_int[::-1]
        if string_int[-1] == "-":
            negative = True
            string_int = string_int[:string_length - 1]
            string_length -= 1
        
        stop = 0
        for i in range(string_length):
            if string_int[i] != "0":
                stop = i
                break
        
        if negative:
            answer = int("-" + string_int[stop:])
        else:
            answer = int(string_int[stop:])

        if answer.bit_length() >= 32:
            return 0
        return answer

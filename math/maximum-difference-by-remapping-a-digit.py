class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Want to find first non-nine
        string_num = str(num)
        max_num = ""
        starting_index = -1
        for i in range(len(string_num)):
            if string_num[i] != '9':
                starting_index = i
                break
        
        if starting_index != -1:
            for char in string_num:
                if char == string_num[starting_index]:
                    max_num += '9'
                else:
                    max_num += char
        else:
            max_num = string_num
        
        starting_index = -1
        for j in range(len(string_num)):
            if string_num[j] != '0':
                starting_index = j
                break
        
        min_num = ""
        if starting_index != -1:
            for char in string_num:
                if char == string_num[starting_index]:
                    min_num += '0'
                else:
                    min_num += char
        else:
            min_num = string_num
        
        return int(max_num) - int(min_num)

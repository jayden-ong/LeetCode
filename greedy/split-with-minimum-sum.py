class Solution:
    def splitNum(self, num: int) -> int:
        string_num = str(num)
        num_list = []
        for char in string_num:
            num_list.append(int(char))
        
        num_list.sort()
        first_num = ""
        second_num = ""
        for i in range(len(num_list)):
            if i % 2 == 0:
                first_num += str(num_list[i])
            else:
                second_num += str(num_list[i])
        return int(first_num) + int(second_num)
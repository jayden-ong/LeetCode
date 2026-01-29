class Solution:
    def minimumSum(self, num: int) -> int:
        string_num = str(num)
        new_list = []
        for char in string_num:
            new_list.append(int(char))
        
        new_list.sort()
        first_num = str(new_list[0]) + str(new_list[2])
        second_num = str(new_list[1]) + str(new_list[3])
        return int(first_num) + int(second_num)
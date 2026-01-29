class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        curr_num = 0
        for num in nums:
            curr_num ^= num
        
        # curr_num stores the two answers
        string_num = format(curr_num, "b")
        for i in range(len(string_num) - 1, -1, -1):
            if string_num[i] == "1":
                indices_from_end = len(string_num) - i
        
        first_num = 0
        second_num = 0
        for num in nums:
            curr_string = format(num, "b")
            if len(curr_string) - indices_from_end >= 0 and curr_string[len(curr_string) - indices_from_end] == "1":
                first_num ^= num
            else:
                second_num ^= num
        return [first_num, second_num]
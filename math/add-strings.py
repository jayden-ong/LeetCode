class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums_dict = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
        strings_dict = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
        num_digits1 = len(num1)
        i = num_digits1 - 1
        num_digits2 = len(num2)
        j = num_digits2 - 1
        carry_over = 0
        curr_ans = ""
        while i > -1 or j > -1:
            if j == -1:
                curr_res = nums_dict[num1[i]] + carry_over
                if curr_res >= 10:
                    curr_ans = "0" + curr_ans
                    carry_over = 1
                else:
                    curr_ans = strings_dict[curr_res] + curr_ans
                    carry_over = 0
                i -= 1
            elif i == -1:
                curr_res = nums_dict[num2[j]] + carry_over
                if curr_res >= 10:
                    curr_ans = "0" + curr_ans
                    carry_over = 1
                else:
                    curr_ans = strings_dict[curr_res] + curr_ans
                    carry_over = 0
                j -= 1
            else:
                curr_res = nums_dict[num1[i]] + nums_dict[num2[j]] + carry_over
                if curr_res >= 10:
                    leftover = curr_res % 10
                    curr_ans = strings_dict[leftover] + curr_ans
                    carry_over = 1
                else:
                    curr_ans = strings_dict[curr_res] + curr_ans
                    carry_over = 0
                i -= 1
                j -= 1
        
        if carry_over > 0:
            curr_ans = "1" + curr_ans
        return curr_ans

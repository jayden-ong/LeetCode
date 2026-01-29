class Solution:
    def numberToWords(self, num: int) -> str:
        nums_dict = {"1" : "One", "2" : "Two", "3" : "Three", "4" : "Four", "5" : "Five", "6" : "Six", "7" : "Seven", "8" : "Eight", "9" : "Nine"}
        nums_above_tens_dict = {"2" : "Twenty", "3" : "Thirty", "4" : "Forty", "5" : "Fifty", "6" : "Sixty", "7" : "Seventy", "8" : "Eighty", "9" : "Ninety"}
        nums_tens_dict = {"0" : "Ten", "1" : "Eleven", "2" : "Twelve", "3" : "Thirteen", "4" : "Fourteen", "5" : "Fifteen", "6" : "Sixteen", "7" : "Seventeen", "8" : "Eighteen", "9" : "Nineteen"}
        millions_dict = {1 : "Thousand", 2 : "Million", 3 : "Billion"}
        def translate_hundreds(str_num):
            answer = ""
            if len(str_num) >= 3 and str_num[0] != "0":
                answer += nums_dict[str_num[0]] + " Hundred"
            
            is_teen = False
            if len(str_num) >= 2:
                if len(str_num) == 2:
                    curr_digit = str_num[0]
                    last_digit = str_num[1]
                else:
                    curr_digit = str_num[1]
                    last_digit = str_num[2]
                
                if curr_digit in "23456789":
                    answer += " " + nums_above_tens_dict[curr_digit]
                elif curr_digit == "1":
                    answer += " " + nums_tens_dict[last_digit]
                    is_teen = True
            
            if not is_teen and str_num[-1] != "0":
                answer += " " + nums_dict[str_num[-1]]
            
            return answer.strip()
        
        if num == 0:
            return "Zero"
        
        string_num = str(num)
        bunches = []
        curr_num = ""
        for i in range(len(string_num) - 1, -1, -1):
            curr_num += string_num[i]
            if len(curr_num) == 3 or i == 0:
                bunches.append(curr_num[::-1])
                curr_num = ""
        
        answer = ""
        for i in range(len(bunches)):
            new_num = translate_hundreds(bunches[i])
            if new_num != "":
                if i in millions_dict:
                    answer = new_num + " " + millions_dict[i] + " " + answer
                else:
                    answer += new_num
        
        return answer.strip()



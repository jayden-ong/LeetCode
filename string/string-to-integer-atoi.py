class Solution:
    def myAtoi(self, s: str) -> int:
        curr_string = s.lstrip()
        length_string = len(curr_string)
        positive = True
        curr = ""
        for i in range(length_string):
            if i == 0 and (curr_string[i] == "+" or curr_string[i] == "-"):
                if curr_string[i] == "-":
                    positive = False
            elif curr_string[i].isnumeric():
                curr += curr_string[i]
            else:
                break
        if curr == "":
            return 0
        
        answer = int(curr)
        if not positive:
            answer *= -1
        
        if answer > pow(2, 31) - 1:
            answer = pow(2, 31) - 1
        elif answer < -pow(2, 31):
            answer = -pow(2, 31)
        return answer
        
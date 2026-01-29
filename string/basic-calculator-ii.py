class Solution:
    def calculate(self, s: str) -> int:
        # Want to get rid of all the multiplication and division 
        stack = []
        curr_num = ""
        spec_oper = ""
        prev = ""
        for i in range(len(s)):
            if s[i] == "-" or s[i] == "+":
                if spec_oper == "/" or spec_oper == "*":
                    if spec_oper == "/":
                        stack.append(int(prev) // int(curr_num))
                    else:
                        stack.append(int(prev) * int(curr_num))
                    spec_oper = ""
                    prev = ""
                    curr_num = ""

                if curr_num != "":
                    stack.append(curr_num)
                    curr_num = ""
                stack.append(s[i])
            elif s[i] == "*" or s[i] == "/":
                if spec_oper == "/" or spec_oper == "*":
                    if spec_oper == "/":
                        prev = int(prev) // int(curr_num)
                    else:
                        prev = int(prev) * int(curr_num)
                    spec_oper = s[i]
                    curr_num = ""
                else:
                    # Once we see these symbols, want to save the current num
                    # Once we see another symbol or the end of the string, we calculate
                    spec_oper = s[i]
                    prev = curr_num
                    curr_num = ""
            elif s[i] in "0123456789":
                curr_num += s[i]
        
        # Want to deal with last number
        if spec_oper == "*":
            stack.append(int(prev) * int(curr_num))
        elif spec_oper == "/":
            stack.append(int(prev) // int(curr_num))
        else:
            stack.append(int(curr_num))
        
        answer = int(stack[0])
        i = 1
        while i < len(stack):
            if stack[i] == "+":
                answer += int(stack[i + 1])
                i += 2
            elif stack[i] == "-":
                answer -= int(stack[i + 1])
                i += 2
        return answer

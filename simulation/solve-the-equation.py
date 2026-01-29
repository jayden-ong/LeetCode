class Solution:
    def solveEquation(self, equation: str) -> str:
        # If you get something like x + something = x + something else, then no solution 
        # If those two somethings are equal, then infinite solutions
        first_equation, second_equation = equation.split("=")
        def get_coeff(equation):
            curr_num = ""
            x_coeff = 0
            non_coeff = 0
            for char in equation:
                # Stop building current num once we hit a "-" or "+" sign
                if char == "-" or char == "+":
                    # It would have been the first character, don't need to reset
                    # If the last character added is "x", then we have to change coeff for "x"
                    if curr_num == "":
                        curr_num += char
                    elif curr_num[-1] == "x":
                        if curr_num == "+x" or curr_num == "x":
                            x_coeff += 1
                        elif curr_num == "-x":
                            x_coeff -= 1
                        else:
                            x_coeff += int(curr_num[:-1])
                        curr_num = "" + char
                    else:
                        non_coeff += int(curr_num)
                        curr_num = "" + char
                else:
                    curr_num += char
                
            if curr_num[-1] == "x":
                if curr_num == "+x" or curr_num == "x":
                    x_coeff += 1
                elif curr_num == "-x":
                    x_coeff -= 1
                else:
                    x_coeff += int(curr_num[:-1])
            else:
                non_coeff += int(curr_num)
            return (x_coeff, non_coeff)

        x_coeff1, non_coeff1 = get_coeff(first_equation)
        x_coeff2, non_coeff2 = get_coeff(second_equation)
        if x_coeff1 == x_coeff2:
            if non_coeff1 == non_coeff2:
                # Ex. x + 5 = x + 5
                return "Infinite solutions"
            else:
                # Ex. x + 5 = x - 4
                return "No solution"
        
        left_coeff = x_coeff1 - x_coeff2
        right_coeff = non_coeff2 - non_coeff1
        answer = right_coeff // left_coeff
        return "x=" + str(answer)
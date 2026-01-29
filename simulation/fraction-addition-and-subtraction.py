class Solution:
    def fractionAddition(self, expression: str) -> str:
        def lcm(a, b):
            if a == b:
                return b
            
            a_increase = a
            b_increase = b
            while a != b:
                if a < b:
                    a += a_increase
                else:
                    b += b_increase
            return a
        
        def reduce(numer, denom):
            if numer == 0:
                return (0, 1)
            for i in range(min(numer, denom), 0, -1):
                if numer % i == 0 and denom % i == 0:
                    return (numer // i, denom // i)
            print(numer)
            print(denom)
        
        answer = "0/1"
        curr_num = ""
        for i in range(len(expression) + 1):
            if i == 0:
                curr_num += expression[i]
            else:
                if i == len(expression) or expression[i] in "+-":
                    # Find lcm for both denom
                    first_frac = answer.split('/')
                    second_frac = curr_num.split('/')
                    first_frac_numer = int(first_frac[0])
                    first_frac_denom = int(first_frac[1])
                    second_frac_numer = int(second_frac[0])
                    second_frac_denom = int(second_frac[1])
                    curr_lcm = lcm(first_frac_denom, second_frac_denom)
                    numerator = first_frac_numer * (curr_lcm // first_frac_denom) + second_frac_numer * (curr_lcm // second_frac_denom)
                    answer = str(numerator) + '/' + str(curr_lcm)
                    
                    if i < len(expression):
                        if expression[i] == '-':
                            curr_num = "-"
                        else:
                            curr_num = ""
                else: 
                    if i < len(expression):
                        curr_num += expression[i]
        numer, denom = answer.split('/')
        if numer[0] == '-':
            new_n, new_d = reduce(int(numer[1:]), int(denom))
            return '-' + str(new_n) + '/' + str(new_d)
        
        new_n, new_d = reduce(int(numer), int(denom))
        return str(new_n) + '/' + str(new_d)
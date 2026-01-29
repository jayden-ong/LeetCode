class Solution:
    def reformat(self, s: str) -> str:
        digits_list = []
        alpha_list = []
        num_digits = 0
        num_alpha = 0
        for char in s:
            if char.isnumeric():
                num_digits += 1
                digits_list.append(char)
            else:
                num_alpha += 1
                alpha_list.append(char)
        
        if abs(num_digits - num_alpha) >= 2:
            return ""
        
        answer = []
        if num_digits > num_alpha:
            answer.append(digits_list.pop())
            first = alpha_list
            second = digits_list
        elif num_digits < num_alpha:
            answer.append(alpha_list.pop())
            first = digits_list
            second = alpha_list
        else:
            first = alpha_list
            second = digits_list

        while digits_list and alpha_list:
            answer.append(first.pop())
            answer.append(second.pop())
        return answer
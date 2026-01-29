class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        curr_ans = 0
        curr_modifier = 1
        if divisor < 0:
            divisor *= -1
            curr_modifier *= -1
        
        if dividend < 0:
            dividend *= -1
            curr_modifier *= -1
        
        if divisor == 1:
            if dividend * curr_modifier > pow(2, 31) - 1:
                return pow(2, 31) - 1
            elif dividend * curr_modifier < -pow(2, 31):
                return -pow(2, 31)
            return dividend * curr_modifier

        curr_ans = len(range(divisor, dividend + 1, divisor))
        
        if curr_ans * curr_modifier > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif curr_ans * curr_modifier < -pow(2, 31):
            return -pow(2, 31)
        return curr_ans * curr_modifier
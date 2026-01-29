class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string_n = str(n)
        digit_prod = 1
        sum_digit = 0
        for str_num in string_n:
            digit_prod *= int(str_num)
            sum_digit += int(str_num)
        
        return digit_prod - sum_digit
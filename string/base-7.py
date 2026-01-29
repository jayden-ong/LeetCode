class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = False
        if num < 0:
            num *= -1
            negative = True
        
        num_bits = 0
        curr_max = 1
        while curr_max <= num:
            curr_max *= 7
            num_bits += 1
        
        if num_bits == 0:
            return "0"
        
        curr_ans = ""
        while num_bits > 0:
            curr_power = num_bits - 1
            curr_divisor = pow(7, curr_power)
            curr_ans += str((num // curr_divisor))
            num = num % curr_divisor
            num_bits -= 1

        if negative:
            return "-" + curr_ans
        return curr_ans
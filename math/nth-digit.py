class Solution:
    def findNthDigit(self, n: int) -> int:
        # 9 one digit numbers
        # 90 two digit numbers
        # 900 three digit numbers
        if n < 10:
            return n
        
        subtract_factor = 9
        num_digits = 1
        while n > subtract_factor:
            n -= subtract_factor
            num_digits += 1
            subtract_factor = 9 * num_digits * pow(10, num_digits - 1)
        
        # n // num_digits tells us which number we are dealing with (want to round up)
        curr_num = int('1' + ('0' * (num_digits - 1))) - 1
        if n % num_digits == 0:
            curr_num += (n // num_digits)
        else:
            curr_num += (n // num_digits) + 1
        n -= 1
        n %= num_digits
        # 1 - 0, 2 - 1, 3 - 0, 4 - 1
        return int(str(curr_num)[n])

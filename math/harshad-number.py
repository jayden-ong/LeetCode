class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        string_x = str(x)
        divisor = 0
        for digit in string_x:
            divisor += int(digit)
        
        if x % divisor == 0:
            return divisor
        return -1
class Solution:
    def maxProduct(self, n: int) -> int:
        highest_num = second_highest_num = float('-inf')
        for digit in str(n):
            digit = int(digit)
            if digit > highest_num:
                highest_num, second_highest_num = digit, highest_num
            elif digit > second_highest_num:
                second_highest_num = digit

        return highest_num * second_highest_num

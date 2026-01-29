class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # If number contains 0, it cannot be included
        def determine_self_divided(num):
            string_num = str(num)
            for digit in string_num:
                if digit == "0":
                    return False 
                elif num % int(digit) != 0:
                    return False
            return True

        res = []
        for i in range(left, right + 1):
            if determine_self_divided(i):
                res.append(i)
        return res
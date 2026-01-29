class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check_no_zeros(num):
            string_num = str(num)
            for char in string_num:
                if char == "0":
                    return False
            return True

        for i in range(1, n):
            if check_no_zeros(i) and check_no_zeros(n - i):
                return [i, n - i]
                
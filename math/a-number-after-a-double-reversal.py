class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        string_num = str(num)
        reversed1 = string_num[::-1]
        new_reversed1 = str(int(reversed1))
        return int(new_reversed1[::-1]) == num
class Solution:
    def largestOddNumber(self, num: str) -> str:
        length_num = len(num)
        for i in range(length_num - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
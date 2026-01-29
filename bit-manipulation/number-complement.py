class Solution:
    def findComplement(self, num: int) -> int:
        string_num = format(num, 'b')
        answer = ""
        for char in string_num:
            if char == '0':
                answer += '1'
            else:
                answer += '0'
        return int(answer, 2)
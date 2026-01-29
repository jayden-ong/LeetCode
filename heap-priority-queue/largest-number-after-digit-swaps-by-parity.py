class Solution:
    def largestInteger(self, num: int) -> int:
        string_num = str(num)
        length_num = len(string_num)
        even_digits = []
        odd_digits = []
        for digit in string_num:
            if int(digit) % 2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)
        
        even_digits.sort(reverse=True)
        odd_digits.sort(reverse=True)
        answer = ""
        even_index = 0
        odd_index = 0
        for i in range(length_num):
            if int(string_num[i]) % 2 == 0:
                answer += even_digits[even_index]
                even_index += 1
            else:
                answer += odd_digits[odd_index]
                odd_index += 1
        return int(answer)
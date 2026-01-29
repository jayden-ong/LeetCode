class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(num):
            string_num = str(num)
            answer = 0
            for digit in string_num:
                answer += int(digit)
            return answer
        
        answer = 0
        for i in range(2, num + 1):
            if digit_sum(i) % 2 == 0:
                answer += 1
        return answer
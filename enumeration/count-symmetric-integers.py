class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def sum_of_digits_equal(string_num):
            mid = len(string_num) // 2
            left = 0
            right = 0
            for i in range(len(string_num)):
                if i < mid:
                    left += int(string_num[i])
                else:
                    right += int(string_num[i])
            return left == right
        
        answer = 0
        for i in range(low, high + 1):
            string_i = str(i)
            if len(string_i) % 2 != 1:
                if sum_of_digits_equal(string_i):
                    answer += 1
        return answer

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        prefix_digits = []
        prefix_sum = []
        curr_digits = ""
        curr_sum = 0
        def convert_digits_to_int(digits):
            answer = 0
            curr = 1
            digits_reverse = digits[::-1]
            for i in range(len(digits)):
                answer += int(digits_reverse[i]) * curr
                curr *= 10
            return answer
        
        for digit in s:
            if digit != "0":
                curr_digits += digit
                curr_sum += int(digit)
            prefix_digits.append(curr_digits)
            prefix_sum.append(curr_sum)

        answer = []
        for left, right in queries:
            if left == 0:
                if prefix_digits[right] == "":
                    answer.append(0)
                else:
                    answer.append((convert_digits_to_int(prefix_digits[right]) * prefix_sum[right]) % MOD)
            else:
                digits = prefix_digits[right][len(prefix_digits[left - 1]):]
                if digits == "":
                    answer.append(0)
                else:
                    curr_sum = prefix_sum[right] - prefix_sum[left - 1]
                    answer.append((convert_digits_to_int(digits) * curr_sum) % MOD)
        return answer
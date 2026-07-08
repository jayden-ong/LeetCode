class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        prefix_digits = []
        prefix_sum = []
        curr_digits = ""
        curr_sum = 0
        for digit in s:
            if digit != "0":
                curr_digits += digit
                curr_sum += int(digit)
            prefix_digits.append(curr_digits)
            prefix_sum.append(curr_sum)
        print(prefix_digits)
        print(prefix_sum)
        answer = []
        for left, right in queries:
            if left == 0:
                answer.append((int(prefix_digits[right]) * prefix_sum[right]) % MOD)
            else:
                digits = prefix_digits[right][len(prefix_digits[left - 1]):]
                if digits == "":
                    answer.append(0)
                else:
                    curr_sum = prefix_sum[right] - prefix_sum[left - 1]
                    answer.append((int(digits) * curr_sum) % MOD)
        return answer
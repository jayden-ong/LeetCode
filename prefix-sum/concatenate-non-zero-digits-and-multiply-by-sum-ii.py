class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        curr_digits_int, prefix_digits_int = 0, []
        prefix_sum = []
        curr_sum = 0
        curr_length, prefix_length = 0, []
        for digit in s:
            if digit != "0":
                curr_sum += int(digit)
                curr_digits_int = (curr_digits_int * 10 + int(digit))
                curr_length += 1
            prefix_sum.append(curr_sum)
            prefix_digits_int.append(curr_digits_int)
            prefix_length.append(curr_length)

        answer = []
        for left, right in queries:
            if left == 0:
                answer.append((prefix_digits_int[right] * prefix_sum[right]) % MOD)
            else:
                curr_sum = prefix_sum[right] - prefix_sum[left - 1]
                diff_in_lengths = prefix_length[right] - prefix_length[left - 1]
                digits_multiple = (prefix_digits_int[right] - prefix_digits_int[left - 1] * pow(10, diff_in_lengths))
                answer.append((digits_multiple * curr_sum) % MOD)
        return answer
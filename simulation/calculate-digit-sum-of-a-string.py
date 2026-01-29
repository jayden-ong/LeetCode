class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def sum_digits(string_num):
            answer = 0
            for char in string_num:
                answer += int(char)
            return str(answer)

        length_s = len(s)
        while length_s > k:
            groups = []
            old_length_s = length_s
            length_s = 0
            for i in range(0, old_length_s, k):
                groups.append(sum_digits(s[i:i + k]))
                length_s += len(groups[-1])
            s = ''.join(groups)
        return s
            
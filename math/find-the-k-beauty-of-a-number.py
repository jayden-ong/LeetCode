class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string_num = str(num)
        length_num = len(string_num)
        answer = 0
        for i in range(length_num - k + 1):
            curr_num = int(string_num[i:i + k])
            if curr_num != 0 and num % curr_num == 0:
                answer += 1
        return answer
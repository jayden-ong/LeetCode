class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length_s = len(s)
        pos_c = []
        num_c = 0
        for i in range(length_s):
            if s[i] == c:
                pos_c.append(i)
                num_c += 1
        
        left = 0
        answer = [0] * length_s
        curr_begin = 0
        while left < num_c:
            for i in range(curr_begin, pos_c[left]):
                answer[i] = pos_c[left] - i
            curr_begin = pos_c[left] + 1
            left += 1
        print(answer)
        right = num_c - 1
        curr_begin = length_s - 1
        while right > -1:
            for i in range(curr_begin, pos_c[right], -1):
                if answer[i] == 0:
                    answer[i] = i - pos_c[right]
                else:
                    answer[i] = min(answer[i], i - pos_c[right])
            curr_begin = pos_c[right] - 1
            right -= 1
        print(answer)
        return answer
        

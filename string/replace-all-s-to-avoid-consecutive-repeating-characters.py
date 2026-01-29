class Solution:
    def modifyString(self, s: str) -> str:
        length_s = len(s)
        answer = ""
        for i in range(length_s):
            if s[i] == '?':
                forbidden = []
                # If the last character was ?, have to look at answer
                if i > 0:
                    forbidden.append(answer[i - 1])
                
                if i < length_s - 1 and s[i + 1] != '?':
                    forbidden.append(s[i + 1])
                
                # Just choose between a, b, and c
                if 'a' not in forbidden:
                    answer += 'a'
                elif 'b' not in forbidden:
                    answer += 'b'
                else:
                    answer += 'c'

            else:
                answer += s[i]
        return answer
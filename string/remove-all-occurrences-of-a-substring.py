class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        curr_index = 0
        answer = ""
        while curr_index < len(s):
            if len(answer) >= len(part) - 1 and answer[len(answer) - len(part) + 1:] + s[curr_index] == part:
                answer = answer[:len(answer) - len(part) + 1]
                curr_index += 1
            else:
                if s[curr_index:curr_index + len(part)] == part:
                    curr_index += len(part)
                else:
                    answer += s[curr_index]
                    curr_index += 1
                
        return answer
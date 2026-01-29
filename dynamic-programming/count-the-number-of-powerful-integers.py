class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def solve(end):
            if len(str(end)) < len(s):
                return 0
            elif len(str(end)) == len(s):
                if int(s) > end:
                    return 0
                return 1
            
            answer = 0
            num_additional_digits = len(str(end)) - len(s)
            suffix = str(end)[num_additional_digits:]
            for i in range(num_additional_digits):
                if int(str(end)[i]) > limit:
                    answer += pow(limit + 1, num_additional_digits - i)
                    return answer
                answer += int(str(end)[i]) * pow(limit + 1, num_additional_digits - i - 1)
            
            if int(suffix) >= int(s):
                answer += 1
            return answer

        return solve(finish) - solve(start - 1)
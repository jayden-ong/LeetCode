class Solution:
    def maxDiff(self, num: int) -> int:
        def convert(is_min):
            answer = ""
            chosen = None
            replacement = None
            for i, digit in enumerate(str(num)):
                if is_min:
                    if chosen is None and i == 0 and digit != "1":
                        chosen = digit
                        replacement = "1"
                        answer += "1"
                    elif chosen is None and i != 0 and digit != "0" and str(num)[0] != digit:
                        chosen = digit
                        replacement = "0"
                        answer += "0"
                    elif chosen == digit:
                        answer += replacement
                    else:
                        answer += digit
                else:
                    if chosen is None and digit != "9":
                        chosen = digit
                        answer += "9"
                    elif chosen == digit:
                        answer += "9"
                    else:
                        answer += digit
            return int(answer)

        return convert(False) - convert(True)
class Solution:
    def processStr(self, s: str, k: int) -> str:
        for char in s:
            if char == "*":
                curr_length = max(curr_length - 1, 0)
            elif char == "#":
                curr_length *= 2
            elif char == "%":
                continue
            else:
                curr_length += 1

        if k >= curr_length:
            return '.'
        
        for char in s[::-1]:
            if char == "*":
                curr_length += 1
            elif char == "#":
                if k >= (length + 1) // 2:
                    k -= length // 2
                length = (length + 1) // 2
            elif char == "%":
                k = length - k - 1
            else:
                if k + 1 == length:
                    return char
                length -= 1
                continue
        return "."
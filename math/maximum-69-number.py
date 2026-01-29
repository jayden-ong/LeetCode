class Solution:
    def maximum69Number (self, num: int) -> int:
        curr = ""
        for i, digit in enumerate(str(num)):
            if digit == "6":
                if i == len(str(num)) - 1:
                    return int(curr + "9")
                return int(curr + "9" + str(num)[i + 1:])
            curr += digit
        return num
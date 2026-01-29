class Solution:
    def hasSameDigits(self, s: str) -> bool:
        curr = s
        while len(curr) != 2:
            new_curr = ""
            for i in range(len(curr) - 1):
                new_curr += str((int(curr[i]) + int(curr[i + 1])) % 10)
            curr = new_curr

        return curr[0] == curr[1]
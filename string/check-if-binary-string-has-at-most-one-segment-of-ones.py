class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_ones = False
        streak = False
        for char in s:
            if char == "1":
                if not found_ones:
                    found_ones = True
                    streak = True
                else:
                    if not streak:
                        return False
            else:
                if found_ones and streak:
                    streak = False
        return True

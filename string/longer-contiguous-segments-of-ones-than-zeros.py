class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_ones_streak = 0
        curr_ones_streak = 0
        longest_zeros_streak = 0
        curr_zeros_streak = 0
        for char in s:
            if char == "0":
                longest_ones_streak = max(longest_ones_streak, curr_ones_streak)
                curr_ones_streak = 0
                curr_zeros_streak += 1
            else:
                longest_zeros_streak = max(longest_zeros_streak, curr_zeros_streak)
                curr_zeros_streak = 0
                curr_ones_streak += 1
        return max(longest_ones_streak, curr_ones_streak) > max(longest_zeros_streak, curr_zeros_streak)
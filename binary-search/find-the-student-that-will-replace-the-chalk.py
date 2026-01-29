class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_remaining = k % sum(chalk)
        for i in range(len(chalk)):
            if chalk_remaining < chalk[i]:
                return i
            chalk_remaining -= chalk[i]
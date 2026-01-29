class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            included = False
            for (start, end) in ranges:
                if i >= start and i <= end:
                    included = True
                    break
            if not included:
                return False
        return True
                
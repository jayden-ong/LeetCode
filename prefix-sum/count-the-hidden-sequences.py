class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Want to figure out what the absolute min and max are
        absolute_min = 0
        absolute_max = 0
        curr = 0
        for difference in differences:
            curr += difference
            absolute_min = min(absolute_min, curr)
            absolute_max = max(absolute_max, curr)
        
        if absolute_max - absolute_min > upper - lower:
            return 0
        
        answer = 0
        if absolute_min <= lower:
            return abs(absolute_max - (upper - (lower - absolute_min))) + 1
        return abs(absolute_min - (lower - (upper - absolute_max))) + 1
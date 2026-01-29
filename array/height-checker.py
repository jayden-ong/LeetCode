class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights.copy()
        sorted_heights.sort()
        num_diffs = 0
        num_heights = len(heights)
        for i in range(num_heights):
            if sorted_heights[i] != heights[i]:
                num_diffs += 1
        return num_diffs
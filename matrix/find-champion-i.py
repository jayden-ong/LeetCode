class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        i = 0
        for row in grid:
            if row.count(1) == len(grid) - 1:
                return i
            i += 1
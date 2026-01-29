class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(y - z) < abs(x - z):
            return 2
        elif abs(y - z) == abs(x - z):
            return 0
        return 1
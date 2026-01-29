class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        num_L = 0
        num_R = 0
        remaining = 0
        for move in moves:
            if move == "L":
                num_L += 1
            elif move == "R":
                num_R += 1
            else:
                remaining += 1
        
        return max(num_L, num_R) - min(num_L, num_R) + remaining
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) % 2 == 0:
            return True
        
        def get_diff(index1, index2):
            if index1 == index2:
                return piles[index1]
            
            return max(piles[index1] - get_diff(index1 + 1, index2), piles[index2] - get_diff(index1, index2 - 1))
        return get_diff(0, len(piles) - 1) >= 0
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Chips on the same parity essentially have the same position
        # Chips on 1, 3, 5, 7 can be moved to each other for no cost
        # Chips on 2, 4, 6, 8 can be moved to each other for no cost
        num_even = 0
        num_odd = 0
        for pos in position:
            if pos % 2 == 0:
                num_even += 1
            else:
                num_odd += 1
        
        if num_even >= num_odd:
            return num_odd
        return num_even
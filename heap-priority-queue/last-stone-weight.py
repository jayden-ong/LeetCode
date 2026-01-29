class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        num_stones = len(stones)
        stones.sort()
        while len(stones) > 1:
            if stones[-2] == stones[-1]:
                stones = stones[:num_stones - 2]
                num_stones -= 2
            else:
                new_stone = stones[-1] - stones[-2]
                stones = stones[:num_stones - 2]
                stones.append(new_stone)
                stones.sort()
                num_stones -= 1

        if num_stones == 0:
            return 0
        else:
            return stones[-1]
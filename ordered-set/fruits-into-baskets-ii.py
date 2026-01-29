class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets_used = set()
        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit and i not in baskets_used:
                    baskets_used.add(i)
                    break
        return len(baskets) - len(baskets_used)
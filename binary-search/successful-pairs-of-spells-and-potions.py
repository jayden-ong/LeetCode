class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        answer = [0] * len(spells)
        potions.sort()
        spells_heap = []
        for i, spell in enumerate(spells):
            heapq.heappush(spells_heap, (-spell, i))
        
        potions_index = 0
        while spells_heap:
            spell, index = heapq.heappop(spells_heap)
            spell *= -1
            while potions_index < len(potions) and potions[potions_index] * spell < success:
                potions_index += 1
            answer[index] = len(potions) - potions_index
        
        return answer
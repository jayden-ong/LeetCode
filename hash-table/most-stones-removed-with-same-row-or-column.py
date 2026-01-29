class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # for every stone, we want to know how many other stones we can remove
        visited = set()
        def find_adjacent(stone_index):
            visited.add(stone_index)
            for i in range(len(stones)):
                if i not in visited and (stones[stone_index][0] == stones[i][0] or stones[stone_index][1] == stones[i][1]):
                    find_adjacent(i)
            
        answer = len(stones)
        for i in range(len(stones)):
            if i not in visited:
                find_adjacent(i)
                answer -= 1
        return answer
        
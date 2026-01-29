class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        potential_champions = set()
        for i in range(n):
            potential_champions.add(i)
        
        for stronger, weaker in edges:
            if weaker in potential_champions:
                potential_champions.remove(weaker)
        
        if len(potential_champions) == 1:
            for champion in potential_champions:
                return champion
        return -1
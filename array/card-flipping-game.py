class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # If a card has the same number on front and back, it cannot be good
        bad_set = set()
        all_nums = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                bad_set.add(fronts[i])
            all_nums.add(fronts[i])
            all_nums.add(backs[i])
        
        all_good = all_nums - bad_set
        if len(all_good) == 0:
            return 0
        return min(all_good)
            
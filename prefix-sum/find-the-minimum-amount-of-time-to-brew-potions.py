class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # when a wizard is done, at least one of them needs to start making the next potion to avoid time waste
        # the earlier the wizard starts, the better
        # Stores the earliest brewing times from previous iteration
        brewing_times = [0] * len(skill)
        for j in range(len(mana)):
            curr = 0
            for i in range(len(skill)):
                curr = max(curr, brewing_times[i]) + skill[i] * mana[j]
            
            brewing_times[-1] = curr
            for i in range(len(skill) - 2, -1, -1):
                brewing_times[i] = brewing_times[i + 1] - skill[i + 1] * mana[j]
        return brewing_times[-1]
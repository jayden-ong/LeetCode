class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        curr_exp = initialExperience
        experience_required = 0
        for person in experience:
            if curr_exp <= person:
                experience_required += person - curr_exp + 1
                curr_exp += person - curr_exp + 1 + person
            else:
                curr_exp += person
        #print(experience_required)
        return max(sum(energy) - initialEnergy + 1, 0) + experience_required
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        desired_skill = sum(skill) // (len(skill) // 2)
        temp = sum(skill) / (len(skill) // 2)
        if desired_skill != temp:
            return -1
        
        answer = 0
        skill.sort()
        for i in range(len(skill) // 2):
            if skill[i] + skill[len(skill) - 1 - i] == desired_skill:
                answer += skill[i] * skill[len(skill) - 1 - i]
            else:
                return -1
        return answer
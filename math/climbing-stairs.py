class Solution:
    def climbStairs(self, n: int) -> int:
        answers_dict = {}
        for i in range(1, n + 1):
            if i == 1:
                answers_dict[i] = 1
            elif i == 2:
                answers_dict[i] = 2
            else:
                answers_dict[i] = answers_dict[i - 1] + answers_dict[i - 2]
        
        return answers_dict[n]
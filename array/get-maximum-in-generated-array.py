class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        answers_dict = {}
        highest = 0
        for i in range(n + 1):
            if i == 0:
                answers_dict[i] = 0
            elif i == 1:
                answers_dict[i] = 1
                highest = max(highest, 1)
            else:
                if i % 2 == 0:
                    answers_dict[i] = answers_dict[i // 2]
                else:
                    answers_dict[i] = answers_dict[i // 2] + answers_dict[(i // 2) + 1]

                highest = max(highest, answers_dict[i])
        return highest
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        answer = [0] * len(questions)
        for i in range(len(questions) - 1, -1, -1):
            num_points, brainpower = questions[i]
            if i + brainpower + 1 >= len(questions):
                if i < len(questions) - 1:
                    answer[i] = max(num_points, answer[i + 1])
                else:
                    answer[i] = num_points
            else:
                answer[i] = max(num_points + answer[i + brainpower + 1], answer[i + 1])
        return answer[0]
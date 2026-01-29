class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for operation in operations:
            if operation == "C":
                score_stack.pop()
            elif operation == "D":
                score_stack.append(score_stack[-1] * 2)
            elif operation == "+":
                score_stack.append(score_stack[-1] + score_stack[-2])
            else:
                score_stack.append(int(operation))
        
        curr_score = 0
        while score_stack:
            curr_score += score_stack.pop()
        return curr_score
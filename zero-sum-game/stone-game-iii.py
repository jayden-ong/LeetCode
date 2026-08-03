class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def solve(curr_index):
            if curr_index == len(stoneValue):
                return 0
        
            answers = []
            if curr_index < len(stoneValue):
                answers.append(stoneValue[curr_index] - solve(curr_index + 1))
            if curr_index < len(stoneValue) - 1:
                answers.append(stoneValue[curr_index] + stoneValue[curr_index + 1] - solve(curr_index + 2))
            if curr_index < len(stoneValue) - 2:
                answers.append(stoneValue[curr_index] + stoneValue[curr_index + 1] + stoneValue[curr_index + 2] - solve(curr_index + 3))
            
            return max(answers)
        
        max_diff = solve(0)
        if max_diff == 0:
            return "Tie"
        elif max_diff > 0:
            return "Alice"
        return "Bob"
                
        

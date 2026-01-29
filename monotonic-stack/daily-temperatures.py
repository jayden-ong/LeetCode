class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [(temperatures[-1], len(temperatures) - 1)]
        for i in range(len(temperatures) - 2, -1, -1):
            # Stack should never be empty
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            if stack:
                answer[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return answer
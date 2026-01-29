class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        curr_string = s
        # Greedy, choose the one that gives most points
        answer = 0
        if x >= y:
            stack = []
            for char in s:
                stack.append(char)
                while len(stack) >= 2 and stack[-2] + stack[-1] == "ab":
                    stack.pop()
                    stack.pop()
                    answer += x
            
            s = ''.join(stack)
            stack = []
            for char in s:
                stack.append(char)
                while len(stack) >= 2 and stack[-2] + stack[-1] == "ba":
                    stack.pop()
                    stack.pop()
                    answer += y
            return answer
        else:
            stack = []
            for char in s:
                stack.append(char)
                while len(stack) >= 2 and stack[-2] + stack[-1] == "ba":
                    stack.pop()
                    stack.pop()
                    answer += y
            
            s = ''.join(stack)
            stack = []
            for char in s:
                stack.append(char)
                while len(stack) >= 2 and stack[-2] + stack[-1] == "ab":
                    stack.pop()
                    stack.pop()
                    answer += x
            return answer
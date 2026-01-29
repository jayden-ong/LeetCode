class Solution:
    def clearDigits(self, s: str) -> str:
        curr_stack = []
        for char in s:
            if char in "0123456789":
                if len(curr_stack) > 0:
                    curr_stack.pop()
            else:
                curr_stack.append(char)
        return ''.join(curr_stack)
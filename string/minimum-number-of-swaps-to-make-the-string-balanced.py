class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for bracket in s:
            if len(stack) > 0 and (bracket == "]" and stack[-1] == "["):
                stack.pop()
            else:
                stack.append(bracket)
        
        if len(stack) == 0:
            return 0
        
        num_unmatched = len(stack) // 2
        if num_unmatched % 2 == 1:
            return num_unmatched // 2 + 1
        return num_unmatched // 2
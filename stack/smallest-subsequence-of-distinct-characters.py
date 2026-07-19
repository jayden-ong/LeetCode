class Solution:
    def smallestSubsequence(self, s: str) -> str:
        num_char_ahead = [0] * 26
        for char in s:
            num_char_ahead[ord(char) - ord('a')] += 1
        seen = set()
        
        stack = []
        for char in s:
            char_num = ord(char) - ord('a')
            num_char_ahead[char_num] -= 1
            if char in seen:
                continue
            
            while stack and ord(stack[-1]) > ord(char) and num_char_ahead[ord(stack[-1]) - ord('a')] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

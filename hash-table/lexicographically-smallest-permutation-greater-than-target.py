class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Idea: choose next smallest char that comes after target's char
        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord('a')] += 1
        
        answer = ""
        prev_chars = ""
        for i in range(ord(target[0]) - ord('a') + 1):
            prev_chars += chars[i] * chr(i + ord('a'))
        curr_answer = ""
        for i in range(ord(target[0]) - ord('a') + 1, 26):
            if chars[i] > 0:
                if curr_answer == "":
                    curr_answer = chr(i + ord('a')) + prev_chars
                    curr_answer += (chars[i] - 1) * chr(i + ord('a'))
                else:
                    curr_answer += chars[i] * chr(i + ord('a'))
            
        if curr_answer == "":
            return ""
        
        if chars[ord(target[0]) - ord('a')] == 0:
            return curr_answer
        
        answer = curr_answer
        # If you match the first letter in target, have to make sure you can still complete string
        # If you don't you can just choose the smallest string after the smallest letter after char in target
        curr_answer = ""
        for char in target:
            success = False
            for i in range(ord(char) - ord('a'), 26):
                if chars[i] > 0:
                    curr_answer += chr(i + ord('a'))
                    chars[i] -= 1
                    success = True
                    break
            
            if not success:
                return answer
        
        if curr_answer > target:
            return curr_answer
        return answer
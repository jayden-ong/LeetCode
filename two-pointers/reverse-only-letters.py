class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        length_s = len(s)
        i = 0
        right = length_s - 1
        curr_answer = []
        while i < length_s:
            if not s[i].isalpha():
                curr_answer.append(s[i])
            else:
                while not s[right].isalpha():
                    right -= 1
                curr_answer.append(s[right])
                right -= 1
            i += 1
        return ''.join(curr_answer)
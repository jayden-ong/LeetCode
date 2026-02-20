class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Number of 1s >= Number of 0s
        curr = start = 0
        special_strings = []
        for i, char in enumerate(s):
            if char == "1":
                curr += 1
            else:
                curr -= 1
            
            # Found special string
            if curr == 0:
                sub_answer = self.makeLargestSpecial(s[start + 1:i])
                special_strings.append("1" + sub_answer + "0")
                start = i + 1
        # Largest ones first
        special_strings.sort(reverse=True)
        answer = ""
        for string in special_strings:
            answer += string
        return answer
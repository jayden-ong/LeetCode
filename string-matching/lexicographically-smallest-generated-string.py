class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        answer = []
        answer_fixed = []
        # Start by filling in the necessary characters according to "T"
        for i, condition in enumerate(str1):
            if condition == "T":
                for j in range(i, i + len(str2)):
                    next_char = str2[j - i]
                    if j >= len(answer):
                        answer.append(next_char)
                        answer_fixed.append("T")
                    else:
                        if answer[j] != next_char and answer_fixed[j] == "T":
                            return ""
                        answer[j] = next_char
                        answer_fixed[j] = "T"
            else:
                if i + len(str2) > len(answer):
                    num_chars_needed = i + len(str2) - len(answer)
                    for k in range(num_chars_needed):
                        answer.append("a")
                        answer_fixed.append("F")
        
        for i, condition in enumerate(str1):
            # Have to make a modification
            if condition == "F" and ''.join(answer[i:i + len(str2)]) == str2:
                fixed = False
                for j in range(i, i + len(str2)):
                    if answer_fixed[j] == "F":
                        # Might have to fix
                        answer[j] = "b"
                        fixed = True
                        break
                
                if not fixed:
                    return ""
        return ''.join(answer)
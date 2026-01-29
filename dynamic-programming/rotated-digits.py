class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Anything with 3, 4 or 7 are automatically invalid
        # Anything with 0, 1 or 8 are invalid if there isn't another digit like 2, 5, 6, or 9
        # Anything without 3, 4 or 7, but also has 2, 5, 6, 9 are valid as long as they are in range
        answer = 0
        for i in range(1, n + 1):
            old_num = str(i)
            new_num = ""
            valid = True
            for j in range(len(old_num)):
                if old_num[j] in "347":
                    valid = False
                    break
                elif old_num[j] == "2":
                    new_num += "5"
                elif old_num[j] == "5":
                    new_num += "2"
                elif old_num[j] == "6":
                    new_num += "9"
                elif old_num[j] == "9":
                    new_num += "6"
                else:
                    new_num += old_num[j]
            
            if valid and old_num != new_num:
                answer += 1
            
        return answer
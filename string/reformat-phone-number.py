class Solution:
    def reformatNumber(self, number: str) -> str:
        new_number = ""
        num_nums = 0
        for char in number:
            if char != "-" and char != " ":
                new_number += char
                num_nums += 1
        
        answer = ""
        i = 0
        while num_nums > 4:
            answer += new_number[i] + new_number[i + 1] + new_number[i + 2] + "-"
            i += 3
            num_nums -= 3
        
        if num_nums == 4:
            answer += new_number[i] + new_number[i + 1] + "-" + new_number[i + 2] + new_number[i + 3]
        elif num_nums == 3:
            answer += new_number[i] + new_number[i + 1] + new_number[i + 2]
        elif num_nums == 2:
            answer += new_number[i] + new_number[i + 1]
        return answer

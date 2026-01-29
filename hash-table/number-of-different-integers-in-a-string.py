class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers_set = set()
        answer = 0
        curr_num = ""
        for char in word:
            if char.isnumeric():
                curr_num += char
            elif curr_num != "":
                if int(curr_num) not in numbers_set:
                    numbers_set.add(int(curr_num))
                    answer += 1
                curr_num = ""
        if curr_num != "" and int(curr_num) not in numbers_set:
            return answer + 1
        return answer
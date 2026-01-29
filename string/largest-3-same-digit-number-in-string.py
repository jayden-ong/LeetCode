class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_streak = 1
        answer = ""
        curr_char = num[0]
        length_num = len(num)
        for i in range(1, length_num):
            if curr_char == num[i]:
                max_streak += 1
            else:
                curr_char = num[i]
                max_streak = 1
            
            if max_streak >= 3 and (answer == "" or int(num[i]) > int(answer)):
                answer = num[i]

        return answer * 3
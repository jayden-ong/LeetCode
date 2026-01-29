class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_hour = int(current[:2])
        correct_hour = int(correct[:2])
        curr_minute = int(current[3:])
        correct_minute = int(correct[3:])
        answer = 0

        if curr_minute > correct_minute:
            curr_hour += 1
            if curr_hour > 23:
                curr_hour = 0
            minutes = 60 - (curr_minute - correct_minute)
        else:
            minutes = correct_minute - curr_minute
            
        while minutes != 0:
            if minutes >= 15:
                minutes -= 15
            elif minutes >= 5:
                minutes -= 5
            else:
                minutes -= 1
            answer += 1
        
        if correct_hour > curr_hour:
            answer += (correct_hour - curr_hour)
        elif curr_hour > correct_hour:
            answer += correct_hour + (24 - curr_hour)
        return answer

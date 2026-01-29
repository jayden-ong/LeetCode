class Solution:
    def maximumTime(self, time: str) -> str:
        # There are always exactly four digits to deal with
        answer = ""
        if time[0] == "?":
            if time[1] == "?" or int(time[1]) < 4:
                answer += "2"
            else:
                answer += "1"
        else:
            answer += time[0]
        
        if time[1] == "?":
            if answer[0] == "2":
                answer += "3"
            else:
                answer += "9"
        else:
            answer += time[1]
        
        answer += ":"

        if time[3] == "?":
            answer += "5"
        else:
            answer += time[3]
        
        if time[4] == "?":
            answer += "9"
        else:
            answer += time[4]
        return answer
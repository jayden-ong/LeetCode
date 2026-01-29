class Solution:
    def countTime(self, time: str) -> int:
        answer = 1
        if time[0] == "?" and time[1] == "?":
            answer *= 24
        elif time[0] == "?" and int(time[1]) < 4:
            answer *= 3
        elif time[0] == "?" and int(time[1]) >= 4:
            answer *= 2
        elif time[0] == "2" and time[1] == "?":
            answer *= 4
        elif time[1] == "?":
            answer *= 10
        
        if time[3] == "?" and time[4] == "?":
            answer *= 60
        elif time[3] == "?":
            answer *= 6
        elif time[4] == "?":
            answer *= 10
        
        return answer
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_time(hour, minutes):
            return int(hour) * 60 + int(minutes)
        
        timePoints.sort()
        answer = float('inf')
        for i in range(len(timePoints)):
            prev = timePoints[i - 1]
            curr = timePoints[i]

            if prev == curr:
                return 0
            
            if i == 0:
                answer = min(answer, 1440 - convert_time(prev[0:2], prev[3:]) + convert_time(curr[0:2], curr[3:]))
            else:
                answer = min(answer, convert_time(curr[0:2], curr[3:]) - convert_time(prev[0:2], prev[3:]))
        return answer
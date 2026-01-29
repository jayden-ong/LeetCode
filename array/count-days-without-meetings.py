class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        heapq.heapify(meetings)
        last_day = 1
        answer = 0
        while meetings:
            start, end = heapq.heappop(meetings)
            if last_day < start:
                answer += start - last_day
            last_day = max(last_day, end + 1)
            print(start)
            print(end)
            print(last_day)
            print(answer)
            print("---")
        
        if last_day <= days:
            answer += days - last_day + 1
        return answer
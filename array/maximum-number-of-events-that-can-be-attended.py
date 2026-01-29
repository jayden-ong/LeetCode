class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events_heap = []
        for start, end in events:
            heapq.heappush(events_heap, (start, end))
        
        answer = 0
        latest_day_heap = []
        curr_day = 0
        while events_heap or latest_day_heap:
            # Need to check if there are any events scheduled on this day
            if not latest_day_heap and events_heap:
                curr_day = events_heap[0][0]
            else:
                curr_day += 1
            
            while events_heap and events_heap[0][0] == curr_day:
                heapq.heappush(latest_day_heap, heapq.heappop(events_heap)[1])
            
            if latest_day_heap:
                answer += 1
                heapq.heappop(latest_day_heap)
                while latest_day_heap and latest_day_heap[0] <= curr_day:
                    heapq.heappop(latest_day_heap)
        
        return answer
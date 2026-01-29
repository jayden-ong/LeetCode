class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # dp? where the val is the max score you can get from day 0 to day n
        events_heap = events.sort()
        start_heap = []
        end_heap = []
        for i, event in enumerate(events):
            start, end, _ = event
            heapq.heappush(start_heap, (start, i))
            heapq.heappush(end_heap, (end, i))
        
        # For each event, want to know next possible event
        next_start = [-1] * len(events)
        while end_heap:
            curr_end, curr_index = heapq.heappop(end_heap)
            while start_heap and start_heap[0][0] <= curr_end:
                heapq.heappop(start_heap)
            
            temp = None
            if start_heap and start_heap[0][1] == curr_index:
                temp = heapq.heappop(start_heap)
            
            if start_heap:
                next_start[curr_index] = start_heap[0][1]
            else:
                next_start[curr_index] = len(events)
            
            if temp:
                heapq.heappush(start_heap, temp)
        
        dp = {}
        def solve(curr_count, curr_index):
            # No more events can be attended
            if curr_count == k or curr_index == len(events):
                return 0
            
            if (curr_count, curr_index) in dp:
                return dp[(curr_count, curr_index)]

            # The two options are to skip or attend
            next_available = next_start[curr_index]
            
            dp[(curr_count, curr_index)] = max(solve(curr_count, curr_index + 1), events[curr_index][2] + solve(curr_count + 1, next_available))
            return dp[(curr_count, curr_index)]
        return solve(0, 0)
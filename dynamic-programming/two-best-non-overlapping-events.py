class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        answer = 0
        # Will contain all of the events we have seen so far, sorted by earliest ending time
        all_processed_events_heap = []
        # Will contain all of the events we have to process
        events_heap = []
        for start, end, score in events:
            heapq.heappush(events_heap, (start, end, score))
        # Will contain all valid events sorted by highest score
        valid_highest_score_heap = []
        while events_heap:
            start_time, end_time, score = heapq.heappop(events_heap)
            # Scheduling one event could be optimal
            answer = max(answer, score)
            # Add previous valid events to score-sorted heap if they ended before this current start time
            while all_processed_events_heap and all_processed_events_heap[0][0] < start_time:
                new_end, new_start, new_score = heapq.heappop(all_processed_events_heap)
                heapq.heappush(valid_highest_score_heap, (-new_score, new_start, new_end))
            
            if valid_highest_score_heap:
                answer = max(answer, score - valid_highest_score_heap[0][0])
            
            heapq.heappush(all_processed_events_heap, (end_time, start_time, score))
        return answer
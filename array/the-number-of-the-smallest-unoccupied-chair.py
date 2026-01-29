class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times_heap = []
        seats_heap = []
        for i in range(len(times)):
            heapq.heappush(times_heap, (times[i][0], times[i][1], i))
            heapq.heappush(seats_heap, i)
        
        sitting_heap = []
        while times_heap:
            # Try looking at times_heap and sitting_heap
            entry_time, entry_leaving_time, entry_friend = heapq.heappop(times_heap)
            
            if sitting_heap:
                leaving_time, curr_seat, leaving_friend = heapq.heappop(sitting_heap)
            else:
                leaving_time = float('inf')
            
            # Current person takes the next available seat
            if entry_time < leaving_time:
                if entry_friend == targetFriend:
                    return heapq.heappop(seats_heap)
                
                # Have to add what was popped back into the sitting_heap
                if leaving_time != float('inf'):
                    heapq.heappush(sitting_heap, (leaving_time, curr_seat, leaving_friend))
                next_seat = heapq.heappop(seats_heap)
                heapq.heappush(sitting_heap, (entry_leaving_time, next_seat, entry_friend))
            elif entry_time == leaving_time:
                heapq.heappush(seats_heap, curr_seat)
                new_seat = heapq.heappop(seats_heap)
                if entry_friend == targetFriend:
                    return new_seat
                
                heapq.heappush(sitting_heap, (entry_leaving_time, new_seat, entry_friend))
            else:
                # Person leaves, undo what was popped from times_heap
                heapq.heappush(times_heap, (entry_time, entry_leaving_time, entry_friend))
                # Put seat back into play
                heapq.heappush(seats_heap, curr_seat)

        # Should never run
        return -1
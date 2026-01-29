class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings_heap = []
        for meeting in meetings:
            heapq.heappush(meetings_heap, meeting)
        
        unoccupied_rooms_heap = []
        for i in range(n):
            heapq.heappush(unoccupied_rooms_heap, i)
        
        # Push end time, room number
        occupied_rooms_heap = []

        answer_dict = defaultdict(int)
        answer = [0, 0]
        def update_answer(answer_dict, curr_answer, curr_room):
            if answer_dict[curr_room] > curr_answer[1] or (answer_dict[curr_room] == curr_answer[1] and curr_room < curr_answer[0]):
                answer[0], answer[1] = curr_room, answer_dict[curr_room]
            
        while meetings_heap:
            start, end = heapq.heappop(meetings_heap)
            # Need to first check if a room being used is done being used
            while occupied_rooms_heap and occupied_rooms_heap[0][0] <= start:
                heapq.heappush(unoccupied_rooms_heap, heapq.heappop(occupied_rooms_heap)[1])
            # If there are unused rooms, the meeting with the earlier start time takes it
            # The lowest numbered rooms get used first
            if unoccupied_rooms_heap:
                room_num = heapq.heappop(unoccupied_rooms_heap)
                heapq.heappush(occupied_rooms_heap, (end, room_num))
                answer_dict[room_num] += 1
                update_answer(answer_dict, answer, room_num)
            else:
                # Need to wait until a room becomes available by forcing out of occupied_rooms_heap
                end_time, room_num = heapq.heappop(occupied_rooms_heap)
                heapq.heappush(occupied_rooms_heap, (end_time + end - start, room_num))
                answer_dict[room_num] += 1
                update_answer(answer_dict, answer, room_num)

        return answer[0]
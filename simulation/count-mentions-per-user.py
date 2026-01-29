class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events_heap = []
        for message, timestamp, ids in events:
            if message == "MESSAGE":
                heapq.heappush(events_heap, (int(timestamp), 1, ids))
            else:
                heapq.heappush(events_heap, (int(timestamp), 0, ids))
            
        mentions = [0 for i in range(numberOfUsers)]
        online = [True for i in range(numberOfUsers)]
        back_online_heap = []
        while events_heap:
            timestamp, message_num, ids = heapq.heappop(events_heap)
            # If enough time has passed, put people back online
            while back_online_heap and back_online_heap[0][0] <= timestamp:
                _, curr_id = heapq.heappop(back_online_heap)
                online[curr_id] = True
            
            # 0 is OFFLINE, 1 is MESSAGE
            if message_num == 0:
                heapq.heappush(back_online_heap, (timestamp + 60, int(ids)))
                online[int(ids)] = False
            else:
                if ids == 'ALL':
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif ids == 'HERE':
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                else:
                    for new_id in ids.split(" "):
                        mentions[int(new_id[2:])] += 1
        return mentions

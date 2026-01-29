class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        roads_dict = defaultdict(list)
        for start, end, time in roads:
            roads_dict[start].append((end, time))
            roads_dict[end].append((start, time))
        
        answer = 0
        pq = []
        heapq.heappush(pq, (0, 0))
        shortest = [float('inf')] * n
        shortest[0] = 0
        num_paths = [0] * n
        num_paths[0] = 1
        while pq:
            curr_time, curr_node = heapq.heappop(pq)
            if curr_time > shortest[curr_node]:
                continue
            
            for destination, time in roads_dict[curr_node]:
                if curr_time + time < shortest[destination]:
                    shortest[destination] = curr_time + time
                    num_paths[destination] = num_paths[curr_node]
                    heapq.heappush(pq, (curr_time + time, destination))
                elif curr_time + time == shortest[destination]:
                    num_paths[destination] += num_paths[curr_node]
        return num_paths[n - 1] % (pow(10, 9) + 7)
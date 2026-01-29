class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        times_dict = {}
        for source, dest, time in times:
            if source in times_dict:
                times_dict[source].append((dest, time))
            else:
                times_dict[source] = [(dest, time)]
        
        # Need to fill up with n vals
        nodes_seen = set()
        # Do not add to nodes_seen unless popped from heap
        nodes_heap = [(0, k)]
        highest_time = 0
        while nodes_heap and len(nodes_seen) != n:
            curr_time, curr_node = heapq.heappop(nodes_heap)
            if curr_node not in nodes_seen:
                if curr_node in times_dict:
                    for dest_node, time in times_dict[curr_node]:
                        if dest_node not in nodes_seen:
                            heapq.heappush(nodes_heap, (curr_time + time, dest_node))
                nodes_seen.add(curr_node)
                highest_time = max(curr_time, highest_time)
        
        if len(nodes_seen) == n:
            return highest_time
        return -1
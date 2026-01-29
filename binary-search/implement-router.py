class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.destination_to_packet = defaultdict(set)
        self.packet_heap = deque()
        self.sorted_packets = {}
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # no dupes
        if (source, destination, timestamp) in self.destination_to_packet[destination]:
            return False
        
        if len(self.packet_heap) == self.limit:
            o_time, o_source, o_dest = self.packet_heap.popleft()
            self.destination_to_packet[o_dest].remove((o_source, o_dest, o_time))
            self.sorted_packets[o_dest].popleft()
        
        self.destination_to_packet[destination].add((source, destination, timestamp))
        self.packet_heap.append((timestamp, source, destination))
        if destination not in self.sorted_packets:
            self.sorted_packets[destination] = deque()
        self.sorted_packets[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_heap:
            return []

        n_time, n_source, n_dest = self.packet_heap.popleft()
        self.destination_to_packet[n_dest].remove((n_source, n_dest, n_time))
        self.sorted_packets[n_dest].popleft()
        return (n_source, n_dest, n_time)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.sorted_packets:
            return 0
        viable_packets = self.sorted_packets[destination]
        right = bisect.bisect_right(viable_packets, endTime)
        left = bisect.bisect_left(viable_packets, startTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

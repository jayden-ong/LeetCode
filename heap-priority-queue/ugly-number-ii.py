class Solution:
    def nthUglyNumber(self, n: int) -> int:
        priority_queue = []
        heapq.heappush(priority_queue, 1)
        num_seen = 0
        all_nums_seen = set()
        all_nums_seen.add(1)
        while True:
            curr_num = heapq.heappop(priority_queue)
            num_seen += 1
            if num_seen == n:
                return curr_num
            
            if curr_num * 2 not in all_nums_seen:
                heapq.heappush(priority_queue, curr_num * 2)
                all_nums_seen.add(curr_num * 2)

            if curr_num * 3 not in all_nums_seen:
                heapq.heappush(priority_queue, curr_num * 3)
                all_nums_seen.add(curr_num * 3)
            
            if curr_num * 5 not in all_nums_seen:
                heapq.heappush(priority_queue, curr_num * 5)
                all_nums_seen.add(curr_num * 5)
        # Should never run
        return -1
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Will now be sorted from earliest to latest start time
        heapq.heapify(intervals)
        curr_interval = heapq.heappop(intervals)
        answer = []
        while intervals:
            next_interval = heapq.heappop(intervals)
            # Means next intervals starts between current interval
            if curr_interval[0] <= next_interval[0] <= curr_interval[1]:
                curr_interval[1] = max(curr_interval[1], next_interval[1])
            else:
                answer.append(curr_interval)
                curr_interval = next_interval

        answer.append(curr_interval)
        return answer
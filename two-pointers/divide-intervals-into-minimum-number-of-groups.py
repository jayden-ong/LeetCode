class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        interval_endings = []
        intervals.sort()
        for left, right in intervals:
            if not interval_endings:
                heapq.heappush(interval_endings, right)
            else:
                smallest_ending = heapq.heappop(interval_endings)
                if left > smallest_ending:
                    heapq.heappush(interval_endings, right)
                else:
                    heapq.heappush(interval_endings, smallest_ending)
                    heapq.heappush(interval_endings, right)

        return len(interval_endings)
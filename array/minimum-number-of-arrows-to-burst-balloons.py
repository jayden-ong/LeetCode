class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heap = []
        answer = 0
        for point in points:
            heapq.heappush(heap, (point[1], point[0]))
        
        # first index is end and second one is start
        while heap:
            answer += 1
            shooting_point, _ = heapq.heappop(heap)
            if heap:
                next_ending, next_starting = heapq.heappop(heap)
                while heap and next_starting <= shooting_point <= next_ending:
                    next_ending, next_starting = heapq.heappop(heap)
                
                if shooting_point < next_starting or shooting_point > next_ending:
                    heapq.heappush(heap, (next_ending, next_starting))
        return answer
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        roads_dict = {}
        for road1, road2 in roads:
            if road1 in roads_dict:
                roads_dict[road1] += 1
            else:
                roads_dict[road1] = 1
            
            if road2 in roads_dict:
                roads_dict[road2] += 1
            else:
                roads_dict[road2] = 1
        
        # Want to assign the highest importance to the road used most often?
        roads_heap = []
        for key in roads_dict:
            heapq.heappush(roads_heap, (-roads_dict[key], key))
        
        answer = 0
        while roads_heap:
            answer += (-heapq.heappop(roads_heap)[0]) * n
            n -= 1
        return answer
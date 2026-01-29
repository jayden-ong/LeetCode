class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap = []
        for i in range(len(names)):
            heapq.heappush(heap, (-heights[i], names[i]))
        
        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[1])
        return answer
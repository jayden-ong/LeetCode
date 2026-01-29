class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        heap = []
        for key in nums_dict:
            heapq.heappush(heap, (-nums_dict[key], key))
        
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer
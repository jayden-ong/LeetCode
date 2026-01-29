class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        
        words_heap = []
        for word in words_dict:
            heapq.heappush(words_heap, (-words_dict[word], word))
        
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(words_heap)[1])
        return answer
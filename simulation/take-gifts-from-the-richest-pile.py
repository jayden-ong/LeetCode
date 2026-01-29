class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        for i in range(k):
            curr_gift = heapq.heappop(heap)
            curr_gift *= -1
            curr_gift = pow(curr_gift, 0.5) // 1
            heapq.heappush(heap, -curr_gift)
        
        answer = 0
        for gift in heap:
            answer += -gift
        return int(answer)
        '''
        while k > 0:
            # Get the max
            most_gifts = max(gifts)
            index_most = gifts.index(most_gifts)
            gifts[index_most] = pow(most_gifts, 0.5) // 1
            k -= 1
        return int(sum(gifts))
        '''
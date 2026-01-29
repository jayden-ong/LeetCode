class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters_heap = []
        if a > 0:
            heapq.heappush(letters_heap, (-a, 'a'))
        
        if b > 0:
            heapq.heappush(letters_heap, (-b, 'b'))
        
        if c > 0:
            heapq.heappush(letters_heap, (-c, 'c'))

        answer = ""
        while letters_heap:
            first_amount, first_choice = heapq.heappop(letters_heap)
            first_amount *= -1
            if len(answer) <= 1 or answer[-1] + answer[-2] != 2 * first_choice:
                answer += first_choice
                first_amount -= 1
                if first_amount > 0:
                    heapq.heappush(letters_heap, (-first_amount, first_choice))
            else:
                # Must pull next letter if it is not 0
                if not letters_heap:
                    return answer
                
                second_amount, second_choice = heapq.heappop(letters_heap)
                second_amount *= -1
                answer += second_choice
                second_amount -= 1
                if second_amount > 0:
                    heapq.heappush(letters_heap, (-second_amount, second_choice))
                
                heapq.heappush(letters_heap, (-first_amount, first_choice))
        return answer
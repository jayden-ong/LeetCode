class Solution:
    def clearStars(self, s: str) -> str:
        letters_heap = []
        for i, letter in enumerate(s):
            if letter == "*":
                heapq.heappop(letters_heap)
            else:
                heapq.heappush(letters_heap, (letter, -i))
        
        answer = [""] * len(s)
        for letter, index in letters_heap:
            answer[-index] = letter
        return ''.join(answer)
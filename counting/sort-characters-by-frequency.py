class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for letter in s_dict:
            heapq.heappush(heap, (-s_dict[letter], letter))
        
        answer = ""
        while heap:
            freq, letter = heapq.heappop(heap)
            freq *= -1
            answer += freq * letter
        return answer
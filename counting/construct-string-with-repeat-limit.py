class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        
        char_heap = []
        for char in char_dict:
            heapq.heappush(char_heap, (26 - (ord(char) - 97), char, char_dict[char]))
        
        answer = ""
        while char_heap:
            pos, char, freq = heapq.heappop(char_heap)
            if len(answer) > 0 and answer[-1] == char:
                # Need to pop another off the heap
                if char_heap:
                    new_pos, new_char, new_freq = heapq.heappop(char_heap)
                    answer += new_char
                    if new_freq > 1:
                        heapq.heappush(char_heap, (new_pos, new_char, new_freq - 1))
                else:
                    return answer
            
            if freq > repeatLimit:
                answer += char * repeatLimit
                heapq.heappush(char_heap, (pos, char, freq - repeatLimit))
            else:
                answer += char * freq
        return answer
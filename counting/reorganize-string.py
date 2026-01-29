class Solution:
    def reorganizeString(self, s: str) -> str:
        letters_dict = {}
        for char in s:
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1

            # If length of string is odd, you can have frequency be 2/3, 5/9, 4/7
            # If length of string is even, you can have 4/8, 5/10, 6/12
            if len(s) % 2 == 1:
                if (letters_dict[char] - 1) / len(s) > 0.5:
                    return ""
            else:
                if letters_dict[char] / len(s) > 0.5:
                    return ""
        
        letters_heap = []
        for letter in letters_dict:
            heapq.heappush(letters_heap, (-letters_dict[letter], letter))
        
        answer = ""
        while letters_heap:
            curr_freq, curr_letter = heapq.heappop(letters_heap)
            if answer != "" and answer[-1] == curr_letter:
                if not letters_heap:
                    return ""
                
                next_freq, next_letter = heapq.heappop(letters_heap)
                answer += next_letter
                heapq.heappush(letters_heap, (curr_freq, curr_letter))
                if next_freq != -1:
                    heapq.heappush(letters_heap, (next_freq + 1, next_letter))
            else:
                answer += curr_letter
                if curr_freq != -1:
                    heapq.heappush(letters_heap, (curr_freq + 1, curr_letter))
        return answer
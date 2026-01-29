class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_heap = []
        for word in words:
            heapq.heappush(words_heap, (-len(word), word))
        
        answer = ""
        words_used = []
        while words_heap:
            curr_length, curr_word = heapq.heappop(words_heap)
            curr_length *= -1
            need_to_add = True
            for word in words_used:
                if word[len(word) - curr_length:] == curr_word:
                    need_to_add = False
                    break
            
            if need_to_add:
                answer += curr_word + "#"
                words_used.append(curr_word)
        return len(answer)
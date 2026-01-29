class Solution:
    def longestWord(self, words: List[str]) -> str:
        prefixes_seen = set()
        prefixes_seen.add("")
        # Want to sort words by length?
        words_heap = []
        for word in words:
            heapq.heappush(words_heap, (len(word), word))
        
        answer = ""
        while words_heap:
            curr_len, curr_word = heapq.heappop(words_heap)
            if curr_word[:curr_len - 1] in prefixes_seen:
                if (curr_len > len(answer)) or (curr_len == len(answer) and curr_word < answer):
                    answer = curr_word
                prefixes_seen.add(curr_word)
        return answer
        
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        letter_dict = defaultdict(int)
        for char in word:
            letter_dict[char] += 1
        
        low_freq_heap = []
        high_freq_heap = []
        for char in letter_dict:
            heapq.heappush(low_freq_heap, (letter_dict[char], char))
            heapq.heappush(high_freq_heap, (-letter_dict[char], char))
        
        answer = float('inf')
        starting_deletions = 0
        while low_freq_heap:
            low_freq, low_freq_char = heapq.heappop(low_freq_heap)
            high_freq_heap_copy = high_freq_heap.copy()
            curr_answer = starting_deletions
            while high_freq_heap and -high_freq_heap_copy[0][0] - low_freq > k:
                curr_answer += -heapq.heappop(high_freq_heap_copy)[0] - low_freq - k
            answer = min(curr_answer, answer)
            starting_deletions += low_freq
        return answer